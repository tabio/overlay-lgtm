import os
from PIL import Image, ImageDraw, ImageFont

text = 'LGTM'

# target-imagesディレクトリからファイル一覧を取得
target_images = [f for f in os.listdir('target-images') if os.path.isfile(os.path.join('target-images', f))]

# target_imagesをループして画像を取得して、textを書き込む
for image_name in target_images:
    if image_name == '.gitkeep':
      continue

    # 画像を取得
    image = Image.open(os.path.join('target-images', image_name))

    # 文字を書き込む
    draw = ImageDraw.Draw(image)

    image_w = image.size[0]
    image_h = image.size[1]

    fontsize = int(image_w / 7) # fontサイズは画像の幅に合わせて調整

    # find /Library/Fonts/ で利用できるfontを探す
    font = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', size=fontsize)

    font_w, font_h = draw.textsize(text, font=font)

    draw.text(((image_w - font_w) / 2, (image_h - font_h) / 2), text, font=font, fill='#ffffff')

    # 画像を保存
    image.save(os.path.join('output-images', image_name))
    print(f'{image_name} is completed.')
