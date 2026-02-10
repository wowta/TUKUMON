export function renderRecords(container, navigate) {
  container.innerHTML = `
    <div class="screen bg-page2">
      <h1>ページ3</h1>

      <button class="image-button bottom-button" id="toHome">
        <img src="img/Top-3 2.png" alt="戻る">
      </button>
    </div>
  `;

  document
    .getElementById("toHome")
    .addEventListener("click", () => {
      navigate("home");
    });
}