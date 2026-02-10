import { renderHome } from "./screens/home.js";
import { renderShop } from "./screens/shop.js";

const app = document.getElementById("app");

const routes = {
  home: renderHome,
  shop: renderShop
};

function navigate(screenName) {
  app.innerHTML = "";
  routes[screenName](app, navigate);
}

// 初期画面
navigate("home");