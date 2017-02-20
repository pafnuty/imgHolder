# ImgHolder

Plugin for SublimeText 2 and 3

Allows you to easily insert a link to a picture-placeholder from [imgholder.ru](https://imgholder.ru/) into html, css, less, sass and scss syntax, with custom size, text & font.

### HTML
![HTML](https://cloud.githubusercontent.com/assets/1635679/23137846/d69639f2-f7bd-11e6-8b4c-e9b1caacad72.png "HTML completions")

### CSS
![CSS](https://cloud.githubusercontent.com/assets/1635679/23137826/bef417a6-f7bd-11e6-8397-9295b7573238.png "CSS completions")

### SASS, LESS etc...
![SASS](https://cloud.githubusercontent.com/assets/1635679/23138032/ae634802-f7be-11e6-8526-40e90cf7a648.png "SASS, LESS etc")

### Markdown
![Markdown](https://cloud.githubusercontent.com/assets/1635679/23137900/1d56a9ee-f7be-11e6-9076-f49e28bee52c.png "Markdown completeons")

### Snippet
![Snippet](https://cloud.githubusercontent.com/assets/1635679/23138325/3019f674-f7c0-11e6-9284-b98c82919ff8.png "Snippet")

## Usage
Trigger autocomplete just after `src="`, `poster="`, `srcset="` or `url(` attributes and select the desired string. Or use snippet on tabTrigger: `imho` or `imgholder`.

## Settings

###InputMask:
`[width]x[height]/[background-color]/[text-color][.ext]&text=[some+text]&font=[font-name]&fz=[50]`

Use `/n` in the text to wrap text to a new line.

## Examples

<a href="https://imgholder.ru/150" target="_blank" title="imgholder.ru/150">
    <img src="https://imgholder.ru/150" alt="imgholder.ru/150">
</a>

<a href="https://imgholder.ru/600x150" target="_blank" title="imgholder.ru/600x150">
    <img src="https://imgholder.ru/600x150" alt="imgholder.ru/600x150">
</a>
<a href="https://imgholder.ru/600x150/aaa/444" target="_blank" title="imgholder.ru/600x150/aaa/444">
    <img src="https://imgholder.ru/600x150/aaa/444" alt="imgholder.ru/600x150/aaa/444">
</a>
<a href="https://imgholder.ru/600x150/666/000" target="_blank" title="imgholder.ru/600x150/666/000">
    <img src="https://imgholder.ru/600x150/666/000" alt="imgholder.ru/600x150/666/000">
</a>
<a href="https://imgholder.ru/600x150/444/eee.jpg" target="_blank" title="imgholder.ru/600x150/444/eee.jpg">
    <img src="https://imgholder.ru/600x150/444/eee.jpg&text=600×150.jpg" alt="imgholder.ru/600x150/444/eee.jpg">
</a>
<a href="https://imgholder.ru/600x150/323232/ccc.jpg&text=image+with+text" target="_blank" title="imgholder.ru/600x150/323232/ccc.jpg&text=image+with+text">
    <img src="https://imgholder.ru/600x150/323232/ccc.jpg&text=image+with+text" alt="imgholder.ru/600x150/323232/ccc.jpg&text=image+with+text">
</a>
<a href="https://imgholder.ru/600x150/272727/FED766&text=image+with+text+and+matias+font&font=matias" target="_blank" title="imgholder.ru/600x150/272727/FED766&text=image+with+text+and+matias+font&font=matias">
    <img src="https://imgholder.ru/600x150/272727/FED766&text=image+with+text+and+matias+font&font=matias" alt="imgholder.ru/600x150/272727/FED766&text=image+with+text+and+matias+font&font=matias">
</a>
<a href="https://imgholder.ru/600x150/A8DADC/1D3557&text=image+with+text+and+corki+font,+size+30&font=corki&fz=30" target="_blank" title="imgholder.ru/600x150/A8DADC/1D3557&text=image+with+text+and+corki+font,+size+30&font=corki&fz=30">
    <img src="https://imgholder.ru/600x150/A8DADC/1D3557&text=image+with+text+and+corki+font,+size+30&font=corki&fz=30" alt="imgholder.ru/600x150/A8DADC/1D3557&text=image+with+text+and+corki+font,+size+30&font=corki&fz=30">
</a>
<a href="https://imgholder.ru/600x150/457B9D/F1FAEE&text=image+with+text/nand+matias+font/nand+size+26/nand+multiline&font=matias&fz=26" target="_blank" title="imgholder.ru/600x150/457B9D/F1FAEE&text=image+with+text/nand+matias+font/nand+size+26/nand+multiline&font=matias&fz=26">
    <img src="https://imgholder.ru/600x150/457B9D/F1FAEE&text=image+with+text/nand+matias+font/nand+size+26/nand+multiline&font=matias&fz=26" alt="imgholder.ru/600x150/457B9D/F1FAEE&text=image+with+text/nand+matias+font/nand+size+26/nand+multiline&font=matias&fz=26">
</a>

### Available font names:
- [roboto](https://imgholder.ru/400x150&text=roboto&font=roboto) (default)
- [arial](https://imgholder.ru/400x150&text=arial&font=arial)
- [bebas](https://imgholder.ru/400x150&text=bebas&font=bebas)
- [bitter](https://imgholder.ru/400x150&text=bitter&font=bitter)
- [corki](https://imgholder.ru/400x150&text=corki&font=corki)
- [debby](https://imgholder.ru/400x150&text=debby&font=debby)
- [fashon fetish](https://imgholder.ru/400x150&text=fashon+fetish&font=ffl)
- [gtw](https://imgholder.ru/400x150&text=gtw&font=gtw)
- [kelson](https://imgholder.ru/400x150&text=kelson&font=kelson)
- [matias](https://imgholder.ru/400x150&text=matias&font=matias)
- [ptsans](https://imgholder.ru/400x150&text=ptsans&font=ptsans)
- [ptsans italic](https://imgholder.ru/400x150&text=ptsans+italic&font=ptsansi)
- [ptserif](https://imgholder.ru/400x150&text=ptserif&font=ptserif)
- [robotoslab](https://imgholder.ru/400x150&text=robotoslab&font=robotoslab)
- [tahoma](https://imgholder.ru/400x150&text=tahoma&font=tahoma)


### Available extensions: 
- [.png](https://imgHolder.ru/300.png)
- [.jpg](https://imgHolder.ru/300.jpg)
- [.gif](https://imgHolder.ru/300.gif)

