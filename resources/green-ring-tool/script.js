const fileInput = document.getElementById("file-input");
const dropZone = document.getElementById("drop-zone");
const resetBtn = document.getElementById("reset-btn");
const zoomRange = document.getElementById("zoom-range");
const sizeSelect = document.getElementById("size-select");
const downloadPngBtn = document.getElementById("download-png");
const downloadJpgBtn = document.getElementById("download-jpg");
const canvas = document.getElementById("avatar-canvas");
const ctx = canvas.getContext("2d");
const ringOverlay = document.getElementById("ring-overlay");

const MAX_FILE_SIZE_MB = 5;
const MIN_DIMENSION = 512;

const state = {
  image: null,
  baseScale: 1,
  zoom: 1,
  offset: { x: 0, y: 0 },
  pointer: {
    active: false,
    start: { x: 0, y: 0 },
    offset: { x: 0, y: 0 },
  },
};

const ringBuffer = document.createElement("canvas");
const ringCtx = ringBuffer.getContext("2d");
let ringReady = false;

function prepareRing() {
  if (!ringOverlay.complete) {
    ringOverlay.addEventListener("load", prepareRing, { once: true });
    return;
  }

  ringBuffer.width = ringOverlay.naturalWidth || canvas.width;
  ringBuffer.height = ringOverlay.naturalHeight || canvas.height;
  ringCtx.clearRect(0, 0, ringBuffer.width, ringBuffer.height);
  ringCtx.drawImage(ringOverlay, 0, 0, ringBuffer.width, ringBuffer.height);
  ringReady = true;
}

prepareRing();

drawPlaceholder();

function drawPlaceholder() {
  const { width, height } = canvas;
  ctx.clearRect(0, 0, width, height);

  const gridSize = 64;
  ctx.save();
  ctx.fillStyle = "rgba(15, 8, 40, 0.85)";
  ctx.fillRect(0, 0, width, height);
  ctx.globalAlpha = 0.4;
  ctx.fillStyle = "#1cff9b";
  for (let x = 0; x < width; x += gridSize) {
    for (let y = 0; y < height; y += gridSize) {
      if ((x + y) / gridSize % 2 === 0) {
        ctx.fillRect(x, y, gridSize, gridSize);
      }
    }
  }
  ctx.restore();

  ctx.strokeStyle = "rgba(60, 255, 234, 0.45)";
  ctx.lineWidth = 4;
  ctx.setLineDash([18, 12]);
  ctx.beginPath();
  ctx.arc(width / 2, height / 2, width * 0.42, 0, Math.PI * 2);
  ctx.stroke();

  ctx.fillStyle = "rgba(241, 246, 255, 0.7)";
  ctx.font = "600 28px 'Rajdhani', 'Segoe UI', sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("Awaiting upload", width / 2, height / 2 + 10);
}

function enableControls(enabled) {
  resetBtn.disabled = !enabled;
  zoomRange.disabled = !enabled;
  sizeSelect.disabled = !enabled;
  downloadPngBtn.disabled = !enabled;
  downloadJpgBtn.disabled = !enabled;
}

function resetState() {
  state.image = null;
  state.baseScale = 1;
  state.zoom = 1;
  state.offset = { x: 0, y: 0 };
  zoomRange.value = "1";
  enableControls(false);
  drawPlaceholder();
}

function handleFile(file) {
  if (!file) return;

  if (!/image\/png|image\/jpeg/.test(file.type)) {
    announce("Unsupported file. Please choose a PNG or JPG.");
    return;
  }

  if (file.size > MAX_FILE_SIZE_MB * 1024 * 1024) {
    announce(`File is larger than ${MAX_FILE_SIZE_MB}MB.`);
    return;
  }

  const image = new Image();
  image.onload = () => {
    if (image.width < MIN_DIMENSION || image.height < MIN_DIMENSION) {
      announce(`Image must be at least ${MIN_DIMENSION}px on each side.`);
      return;
    }

    state.image = image;
    computeBaseScale();
    state.zoom = 1;
    zoomRange.value = "1";
    state.offset = { x: 0, y: 0 };
    enableControls(true);
    draw();
    announce("Image loaded. Use zoom and drag to align inside the halo.");
  };
  image.onerror = () => announce("Unable to read that image. Try a different file.");

  const reader = new FileReader();
  reader.onload = (event) => {
    image.src = event.target.result;
  };
  reader.readAsDataURL(file);
}

function computeBaseScale() {
  if (!state.image) return;
  const scale = Math.max(canvas.width / state.image.width, canvas.height / state.image.height);
  state.baseScale = scale;
}

function clampOffset() {
  if (!state.image) return;
  const scale = state.baseScale * state.zoom;
  const drawWidth = state.image.width * scale;
  const drawHeight = state.image.height * scale;
  const maxOffsetX = Math.max(0, (drawWidth - canvas.width) / 2);
  const maxOffsetY = Math.max(0, (drawHeight - canvas.height) / 2);
  state.offset.x = Math.min(maxOffsetX, Math.max(-maxOffsetX, state.offset.x));
  state.offset.y = Math.min(maxOffsetY, Math.max(-maxOffsetY, state.offset.y));
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  if (!state.image) {
    drawPlaceholder();
    return;
  }

  const scale = state.baseScale * state.zoom;
  const drawWidth = state.image.width * scale;
  const drawHeight = state.image.height * scale;
  const drawX = canvas.width / 2 - drawWidth / 2 + state.offset.x;
  const drawY = canvas.height / 2 - drawHeight / 2 + state.offset.y;

  ctx.save();
  ctx.fillStyle = "rgba(5, 0, 20, 0.9)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(state.image, drawX, drawY, drawWidth, drawHeight);
  ctx.restore();
}

function announce(message) {
  dropZone.setAttribute("data-status", message);
  dropZone.title = message;
}

function onPointerDown(event) {
  if (!state.image) return;
  state.pointer.active = true;
  state.pointer.start = { x: event.clientX, y: event.clientY };
  state.pointer.offset = { ...state.offset };
  canvas.setPointerCapture(event.pointerId);
}

function onPointerMove(event) {
  if (!state.pointer.active) return;
  const dx = event.clientX - state.pointer.start.x;
  const dy = event.clientY - state.pointer.start.y;
  state.offset.x = state.pointer.offset.x + dx;
  state.offset.y = state.pointer.offset.y + dy;
  clampOffset();
  draw();
}

function onPointerUp(event) {
  if (!state.pointer.active) return;
  state.pointer.active = false;
  canvas.releasePointerCapture(event.pointerId);
}

function onZoomChange(event) {
  if (!state.image) return;
  state.zoom = Number(event.target.value);
  clampOffset();
  draw();
}

async function exportImage(type) {
  if (!state.image) return;
  const size = Number(sizeSelect.value);
  const exportCanvas = document.createElement("canvas");
  exportCanvas.width = size;
  exportCanvas.height = size;
  const exportCtx = exportCanvas.getContext("2d");

  const scaleFactor = size / canvas.width;
  const scale = state.baseScale * state.zoom * scaleFactor;
  const drawWidth = state.image.width * scale;
  const drawHeight = state.image.height * scale;
  const drawX = size / 2 - drawWidth / 2 + state.offset.x * scaleFactor;
  const drawY = size / 2 - drawHeight / 2 + state.offset.y * scaleFactor;

  exportCtx.fillStyle = "rgba(5, 0, 20, 1)";
  exportCtx.fillRect(0, 0, size, size);
  exportCtx.drawImage(state.image, drawX, drawY, drawWidth, drawHeight);

  if (ringReady) {
    exportCtx.drawImage(ringBuffer, 0, 0, size, size);
  }

  const blob = await new Promise((resolve) =>
    exportCanvas.toBlob(resolve, type, type === "image/jpeg" ? 0.92 : undefined)
  );

  if (!blob) {
    announce("Export failed. Try again.");
    return;
  }

  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `agent-halo-${size}.${type === "image/png" ? "png" : "jpg"}`;
  link.click();
  URL.revokeObjectURL(url);
}

function handleDrop(event) {
  event.preventDefault();
  dropZone.classList.remove("dragover");
  const file = event.dataTransfer.files?.[0];
  handleFile(file);
}

function handleDrag(event) {
  event.preventDefault();
  if (event.type === "dragover") {
    dropZone.classList.add("dragover");
  } else {
    dropZone.classList.remove("dragover");
  }
}

fileInput.addEventListener("change", (event) => handleFile(event.target.files?.[0]));

resetBtn.addEventListener("click", resetState);
zoomRange.addEventListener("input", onZoomChange);
sizeSelect.addEventListener("change", () => state.image && draw());
downloadPngBtn.addEventListener("click", () => exportImage("image/png"));
downloadJpgBtn.addEventListener("click", () => exportImage("image/jpeg"));

dropZone.addEventListener("click", () => fileInput.click());
dropZone.addEventListener("dragover", handleDrag);
dropZone.addEventListener("dragleave", handleDrag);
dropZone.addEventListener("drop", handleDrop);

canvas.addEventListener("pointerdown", onPointerDown);
canvas.addEventListener("pointermove", onPointerMove);
canvas.addEventListener("pointerup", onPointerUp);
canvas.addEventListener("pointercancel", onPointerUp);

resetState();
