let imgBorder = document.querySelector(".img-border")
let imgNumber1 = document.querySelector(".img-number1")


if (document.dir === "rtl") {
imgBorder.style.display = "inline-block"
    imgNumber1.style.display = "inline-block!important"
} else if (document.dir === "ltr") {
    imgBorder.style.display = "none"
    imgNumber1.style.display = "none"
}

