// 1)შექმენით რამდენიმე თეგი HTML-ში და javascript-ის გამოყენებით მიეცით სასურველი სტილები და შეუცვალეთ კონტენტი

let h1 = document.getElementsByTagName("h1")
let p = document.getElementsByTagName("p")

h1[0].style.color = "RED"

p[0].style.color = "GREEN"
p[1].style.color = "BLUE"

h1[0].innerHTML = "cw"
p[0].innerHTML = "Nika"
p[1].innerHTML = "Monaselidze"