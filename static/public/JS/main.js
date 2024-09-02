let menuButton = document.querySelector(".nav-btn")
let imgBorder = document.querySelector(".img-border")
let blurBackground = document.querySelector(".blur-background ")
let imgNumber1 = document.querySelector(".img-number1")
let navList = document.querySelector(".nav-list")
let navLogo = document.querySelector(".nav-logo")


let is_show = false


if (document.dir === "rtl") {
    navLogo.style.left = " 17px";
    menuButton.style.right = "0px";
    // imgBorder.style.display = "inline-block"
    // imgNumber1.style.display = "inline-block!important"
} else if (document.dir === "ltr") {
    // imgBorder.style.display = "none"
    // imgNumber1.style.display = "none"
    navLogo.style.right = " 17px"
    menuButton.style.left = "0px";
}

const onClickMenuButton = () => {
    if (window.innerWidth < 480) {
        if (is_show === false) {
            blurBackground.style.height = "95dvh"
            navList.style.display = "flex"
            navList.style.height = "470px"
            is_show = true
        }
        else {
            window.document.body.style.overflowY = "scroll"
            blurBackground.style.height = "0px";
            navList.style.display = "none"
            navList.style.height = "0px"
            is_show = false

        }

    }
    else return

}



menuButton.addEventListener("click", onClickMenuButton)






var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        '730': {
            slidesPerView: 4,
            spaceBetween: 40,
        }
    }
});

const onCloseMenu = () => {
    onClickMenuButton()
}





