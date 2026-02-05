import asyncio
import os
import sys
from pathlib import Path
import pygame

# iPhone 12 論理解像度
SCREEN_WIDTH = 390
SCREEN_HEIGHT = 844
BACKGROUND_COLOR = (201, 226, 215)  # #F0F0F0
FPS = 60

# 画像フォルダのパス
IMG_FOLDER = Path(__file__).parent / "img"


def load_images():
    """img フォルダから全画像を読み込む"""
    images = []
    
    if not IMG_FOLDER.exists():
        print(f"警告: {IMG_FOLDER} フォルダが見つかりません")
        return images
    
    # 対応する画像形式
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    
    try:
        image_files = sorted([
            f for f in IMG_FOLDER.iterdir()
            if f.is_file() and f.suffix.lower() in supported_formats
        ])
        
        for image_file in image_files:
            try:
                image = pygame.image.load(str(image_file))
                images.append(image)
                print(f"読み込み成功: {image_file.name}")
            except pygame.error as e:
                print(f"警告: {image_file.name} の読み込みに失敗しました: {e}")
            except Exception as e:
                print(f"エラー: {image_file.name} の処理中にエラーが発生しました: {e}")
        
        print(f"合計 {len(images)} 個の画像を読み込みました")
    except Exception as e:
        print(f"エラー: img フォルダのスキャン中にエラーが発生しました: {e}")
    
    return images


def scale_image(image, screen_width, screen_height):
    """
    画像をアスペクト比を維持したまま、画面にフィットするようリサイズ
    """
    img_width, img_height = image.get_size()
    
    # 幅に基づくスケーリング
    scale_by_width = screen_width / img_width
    # 高さに基づくスケーリング
    scale_by_height = screen_height / img_height
    
    # 小さい方のスケールを採用（画像が画面を超えないように）
    scale = min(scale_by_width, scale_by_height)
    
    new_width = int(img_width * scale)
    new_height = int(img_height * scale)
    
    return pygame.transform.scale(image, (new_width, new_height))


def get_centered_rect(image, screen_width, screen_height):
    """
    スケール済みの画像を画面中央に配置するためのrectを取得
    """
    rect = image.get_rect()
    rect.center = (screen_width // 2, screen_height // 2)
    return rect


async def main():
    """メインループ"""
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Image Overlay - iPhone 12")
    clock = pygame.time.Clock()
    
    # 画像を読み込む
    raw_images = load_images()
    
    # 画像をスケーリング
    scaled_images = []
    image_rects = []
    
    for raw_image in raw_images:
        scaled = scale_image(raw_image, SCREEN_WIDTH, SCREEN_HEIGHT)
        scaled_images.append(scaled)
        rect = get_centered_rect(scaled, SCREEN_WIDTH, SCREEN_HEIGHT)
        image_rects.append(rect)
    
    print(f"アプリ起動: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # 背景を描画
        screen.fill(BACKGROUND_COLOR)
        
        # 全ての画像を中央に重ねて描画
        for scaled_image, rect in zip(scaled_images, image_rects):
            screen.blit(scaled_image, rect)
        
        # 画面更新
        pygame.display.flip()
        clock.tick(FPS)
        
        # asyncio 統合
        await asyncio.sleep(0)
    
    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
