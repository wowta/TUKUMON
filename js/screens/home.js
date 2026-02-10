export function renderHome(container, navigate) {
  container.innerHTML = `
    <div class="screen">

      <!-- 背景 -->
      <div class="bg">
        <img src="img/Top-1 2.png" alt="">
      </div>

      <!-- 上部左右UI -->
      <div class="top-ui">
        <img src="img/Top-3 2.png" alt="左上UI">
        <img src="img/Top-10 2.png" alt="右上UI">
      </div>

      <!-- キャラクター＋吹き出し -->
      <div class="character-area">
        <img class="balloon" src="img/Top-8 2.png" alt="吹き出し">
        <img class="character" src="img/Top-7 2.png" alt="キャラクター">
      </div>

      <!-- 下部横長UI -->
      <div class="bottom-ui">
        <img src="img/Top-2 2.png" alt="下部UI">
      </div>

      <!-- 下部ボタン3つ -->
      <div class="button-area">
        <button id="btn1">
          <img src="img/Top-5 2.png" alt="ボタン1">
        </button>
        <button id="btn2">
          <img src="img/Top-4 2.png" alt="ボタン2">
        </button>
        <button id="btn3">
          <img src="img/Top-6 2.png" alt="ボタン3">
        </button>
      </div>

    </div>
  `;

  document.getElementById("btn1").addEventListener("click", () => {
    navigate("records");
  });
  document.getElementById("btn2").addEventListener("click", () => {
    navigate("shop");
  });
}
