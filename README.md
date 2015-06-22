# ImgHolder

Plugin for SublimeText 2 and 3

Allows you to easily insert a link to a picture-placeholder from [imgholder.ru](http://imgholder.ru/) into html, css, less and sass syntax, with custom size, text & font. **Support for http or https.**

### HTML
![HTML](https://dl.dropboxusercontent.com/u/8142395/imgholder/1.png "HTML completions")
### CSS
![CSS](https://dl.dropboxusercontent.com/u/8142395/imgholder/2.png "CSS completions")
### SASS
![SASS](https://dl.dropboxusercontent.com/u/8142395/imgholder/3.png "SASS completions")
### LESS
![LESS](https://dl.dropboxusercontent.com/u/8142395/imgholder/4.png "LESS completions")
### Snippet
![Snippet](https://dl.dropboxusercontent.com/u/8142395/imgholder/5.png "Snippet")

## Usage

Trigger autocomplete just after **src="** or **url(** attributes and select the desired string. Or use snippet on tabTrigger: `imho` or `imgholder`.

## Settings

###InputMask:
`[width]x[height]/[background-color]/[text-color][.ext]&text=[some+text]&font=[font-name]`

###For example
[//imgholder.ru/150](https:////imgholder.ru/150)
[//imgholder.ru/600x300](https:////imgholder.ru/600x300)
[//imgholder.ru/600x300/444](https:////imgholder.ru/600x300/444)
[//imgholder.ru/600x300/444/ссс](https:////imgholder.ru/600x300/444/ссс)
[//imgholder.ru/600x300/444/ссс.jpg](https:////imgholder.ru/600x300/444/ссс.jpg)
[//imgholder.ru/600x300/444/ссс.jpg&text=привет+как+дела](https:////imgholder.ru/600x300/444/ссс.jpg&text=привет+как+дела)
[//imgholder.ru/600x300/444/ссс.jpg&text=привет+как+дела&font=bebas](https:////imgholder.ru/600x300/444/ссс.jpg&text=привет+как+дела&font=bebas)


### Available font names:
- roboto (default)
- arial
- tahoma
- kelson
- gtw
- bebas
- robotoslab
- ptserif
- bitter
- corki

### Available extensions: 
- .png
- .jpg
- .gif

