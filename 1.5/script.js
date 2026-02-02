// Дані підрозділів
const units = [
  { unit_id: 101, name: "1 окрема механізована бригада", type: "механізована", corps: "ОК Північ", personnel: 3200, status: "виконує бойове завдання", location: "Сіверський напрямок", last_report: "2026-01-22" },
  { unit_id: 102, name: "25 окрема десантно-штурмова бригада", type: "десантно-штурмова", corps: "ОК Схід", personnel: 2800, status: "резерв", location: "Краматорськ", last_report: "2026-01-22" },
  { unit_id: 103, name: "40 артилерійська бригада", type: "артилерійська", corps: "ОК Південь", personnel: 2100, status: "веде вогневу підтримку", location: "Запорізький напрямок", last_report: "2026-01-21" },
  { unit_id: 104, name: "92 окрема штурмова бригада", type: "штурмова", corps: "ОК Схід", personnel: 3500, status: "активні бойові дії", location: "Бахмутський напрямок", last_report: "2026-01-22" },
  { unit_id: 105, name: "128 окрема гірсько-штурмова бригада", type: "гірсько-штурмова", corps: "ОК Захід", personnel: 3000, status: "оборона", location: "Херсонський напрямок", last_report: "2026-01-20" }
];

// Визначаємо кольори карток по типу
function getTone(type) {
  switch(type) {
    case "механізована": return "tone-green";
    case "десантно-штурмова": return "tone-blue";
    case "артилерійська": return "tone-amber";
    case "штурмова": return "tone-red";
    case "гірсько-штурмова": return "tone-iron";
    default: return "tone-iron";
  }
}

// Створення картки підрозділу
function createCard(unit) {
  const card = document.createElement("article");
  card.className = "card " + getTone(unit.type);
  card.innerHTML = `
    <h3>${unit.name}</h3>
    <p><strong>Тип:</strong> ${unit.type}</p>
    <p><strong>Корпус:</strong> ${unit.corps}</p>
    <p><strong>Чисельність:</strong> ${unit.personnel}</p>
    <p><strong>Статус:</strong> ${unit.status}</p>
    <p><strong>Локація:</strong> ${unit.location}</p>
    <p><strong>Останній звіт:</strong> ${unit.last_report}</p>
  `;
  return card;
}

// Відображення карток
function renderUnits(filtered = units) {
  const grid = document.querySelector(".card-grid");
  grid.innerHTML = "";
  filtered.forEach(unit => grid.appendChild(createCard(unit)));
}

// Фільтрація
function filterUnits() {
  const corpsFilter = document.getElementById("filter-corps").value;
  const statusFilter = document.getElementById("filter-status").value;

  const filtered = units.filter(u => {
    return (corpsFilter === "all" || u.corps === corpsFilter) &&
           (statusFilter === "all" || u.status === statusFilter);
  });

  renderUnits(filtered);
}

// Лінійний пошук
function linearSearch(query) {
  query = query.toLowerCase();
  return units.filter(u => u.name.toLowerCase().includes(query));
}

// Бінарний пошук
function binarySearch(query) {
  query = query.toLowerCase();
  const sorted = [...units].sort((a, b) => a.name.localeCompare(b.name));
  let left = 0, right = sorted.length - 1;
  const results = [];
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const midName = sorted[mid].name.toLowerCase();
    if (midName.includes(query)) {
      let i = mid;
      while (i >= 0 && sorted[i].name.toLowerCase().includes(query)) { results.push(sorted[i]); i--; }
      i = mid + 1;
      while (i < sorted.length && sorted[i].name.toLowerCase().includes(query)) { results.push(sorted[i]); i++; }
      break;
    } else if (midName < query) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return results;
}

// Обробник кнопки пошуку
document.getElementById("btn-search").addEventListener("click", () => {
  const query = document.getElementById("search-input").value.trim();
  const method = document.getElementById("search-method").value;
  if (!query) {
    renderUnits();
    return;
  }
  const results = method === "linear" ? linearSearch(query) : binarySearch(query);
  renderUnits(results);
});

// Ініціалізація
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("filter-corps").addEventListener("change", filterUnits);
  document.getElementById("filter-status").addEventListener("change", filterUnits);
  renderUnits();
});
