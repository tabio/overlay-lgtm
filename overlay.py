import os
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *


text = 'LGTM'

# target-imagesディレクトリからファイル一覧を取得
target_images = [f for f in os.listdir('target-images') if os.path.isfile(os.path.join('target-images', f))]

def normal(image_name):
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


def gif(image_name):
    # 元のGIFファイルを読み込む
    input_file = os.path.join('target-images', image_name)
    output_file = os.path.join('output-images', image_name)
    original_clip = VideoFileClip(input_file)

    # テキストを追加
    image = Image.open(input_file)
    image_w = image.size[0]
    image_h = image.size[1]

    fontsize = int(image_w / 7) # fontサイズは画像の幅に合わせて調整
    font = '/Library/Fonts/Arial Unicode.ttf'
    txt_clip = TextClip('LGTM', fontsize=fontsize, color='white', font=font)
    txt_clip = txt_clip.set_pos('center').set_duration(original_clip.duration)

    # テキストを合成
    video = CompositeVideoClip([original_clip, txt_clip])

    # 出力ファイルに保存
    video.write_gif(output_file, fps=original_clip.fps)


# target_imagesをループして画像を取得して、textを書き込む
for image_name in target_images:
    if image_name == '.gitkeep':
      continue

    if image_name.endswith('.gif'):
        gif(image_name)
    else:
        normal(image_name)

