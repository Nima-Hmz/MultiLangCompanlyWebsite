let imgBorder = document.querySelector(".img-border")
let imgNumber2 = document.querySelector(".img-number-2")
let imgNumber1 = document.querySelector(".img-number1")



if (document.dir === "rtl") {
    imgBorder.style.display = "inline-block"
    imgNumber2.style.display = "inline-block!important"
    imgNumber1.style.width = "210px"
} else if (document.dir === "ltr") {
    imgBorder.style.display = "none"
    imgNumber1.style.marginLeft = "-115px"
}

