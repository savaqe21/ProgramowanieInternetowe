const STORAGE_KEY = 'clickCountVisitCounter';

const clickBtn = document.getElementById('click-btn');
const resetBtn = document.getElementById('reset-btn');
const clickDisplay = document.getElementById('click-count');

// Wczytywanie localstorage
let clickCount = parseInt(localStorage.getItem(STORAGE_KEY)) || 0;

clickDisplay.textContent = clickCount;

function updateCount(newCount) {
  clickCount = newCount;
  localStorage.setItem(STORAGE_KEY, clickCount);
  clickDisplay.textContent = clickCount;
}

// Klikanie
clickBtn.addEventListener('click', () => {
  updateCount(clickCount + 1);
});

// Reset
resetBtn.addEventListener('click', () => {
  if (confirm('Czy na pewno chcesz zresetować licznik kliknięć?')) {
    updateCount(0);
  }
});
