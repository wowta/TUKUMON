import { state } from "../state.js";
export function renderRecords(container, navigate) {
  container.innerHTML = `
    <div class="screen bg-page2">

      <!-- 背景 -->
      <div class="bg">
        <img src="img/list-2.png" alt="">
      </div>

      <!-- 上部左右UI -->
      <div class="top-ui">
        <img src="img/Top-3 2.png" alt="左上UI">
        <div class="level">
        ${state.level}</div>
        <div class="point">
        <img src="img/Top-2 2.png" alt="右上UI"></div>
        <div class="top-point">
        ${state.point}</div>
        <div class="config">
        <img src="img/Top-10 2.png" alt="右上UI"></div>
      </div>
      <div class="records">
        <img src="img/list-4.png" alt="左上UI">
        <img src="img/list-3.png" alt="右上UI">
      </div>

      <!-- 戻るボタン -->
      <button class="return" id="toHome">
        <img src="img/list-1.png" alt="戻る">
      </button>
    </div>
  `;

  document
    .getElementById("toHome")
    .addEventListener("click", () => {
      navigate("home");
    });
}