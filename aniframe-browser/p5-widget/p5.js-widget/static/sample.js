function setup() {createCanvas(1000, 1000);}
function draw() {
    background("#FFFFFF");
push();
if (100 <= frameCount && frameCount <= 200) {
    new _car1().display();
}
if (201 <= frameCount && frameCount <= 250) {
    translate(new p5.Vector(frameCount - 200 + 10, frameCount - 200 + 20));
new _car1().display();
}
if (251 <= frameCount && frameCount <= 300) {
    translate(new p5.Vector(frameCount - 200 + 10, frameCount - 200 + 20));
rotate((frameCount - 250) * radians(45) / (300 - 250 + 1));
new _car1().display();
}
if (301 <= frameCount && frameCount <= 400) {
    translate(new p5.Vector(300 - 200 + 10, 300 - 200 + 20));
rotate((300 - 250) * radians(45) / (300 - 250 + 1));
new _car1().display();
}
if (401 <= frameCount && frameCount <= 10000000000000000159028911097599180468360808563945281389781327557747838772170381060813469985856815104) {
    translate(new p5.Vector(300 - 200 + 10, 300 - 200 + 20));
rotate((300 - 250) * radians(45) / (300 - 250 + 1));
}
pop();
push();
if (1 <= frameCount && frameCount <= 400) {
    new _star().display();
}
pop();
push();
if (50 <= frameCount && frameCount <= 400) {
    new _dog().display();
}
pop();
}

class _car_body {
    constructor() {
    }
    display() {
fill("#ADD8E6");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
    }
}
class _wheel1 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#ADD8FF");
circle(80, 80, 33);
    }
}
class _window1 {
    constructor() {
    }
    display() {
fill("#000000");
stroke("#000000");
triangle(30, 75, 58, 20, 86, 75);
    }
}
class _car {
    constructor() {
    }
    display() {
    }
}
class _$0 {
    constructor() {
    }
    display() {
fill("#ADD8E6");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
    }
}
class _$1 {
    constructor() {
    }
    display() {
fill("#000000");
stroke("#000000");
triangle(30, 75, 58, 20, 86, 75);
    }
}
class _$2 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#ADD8FF");
circle(80, 80, 33);
    }
}
class _car_body1 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
    }
}
class _wheel11 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
circle(280, 280, 33);
    }
}
class _window11 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
    }
}
class _$3 {
    constructor() {
    }
    display() {
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
    }
}
class _car1 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
circle(280, 280, 33);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
circle(280, 280, 33);
fill("#FFFFFF");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
    }
}
class _$4 {
    constructor() {
    }
    display() {
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
    }
}
class _$5 {
    constructor() {
    }
    display() {
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
fill("#FFFFFF");
stroke("#ADD8FF");
circle(280, 280, 33);
    }
}
class _$6 {
    constructor() {
    }
    display() {
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
fill("#FFFFFF");
stroke("#ADD8FF");
circle(280, 280, 33);
    }
}
class _$7 {
    constructor() {
    }
    display() {
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
fill("#FFFFFF");
stroke("#ADD8FF");
circle(280, 280, 33);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#ADD8E6");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#000000");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
fill("#FFFFFF");
stroke("#ADD8FF");
circle(280, 280, 33);
    }
}
class _star {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
beginShape();
vertex(30, 20);
vertex(85, 20);
vertex(85, 75);
vertex(30, 75);
endShape(CLOSE);
    }
}
class _dog {
    constructor() {
    }
    display() {
fill("#000000");
stroke("#000000");
text("awooo", 80, 90);
    }
}
class _bird_torso {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(30, 20, 55, 55);
    }
}
class __0 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(30, 20, 55, 55);
    }
}
class __1 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
    }
}
class __2 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
circle(280, 280, 33);
    }
}
class __3 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
    }
}
class __4 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
    }
}
class _$8 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
    }
}
class __5 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
    }
}
class _$9 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
    }
}
class __6 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
circle(280, 280, 33);
    }
}
class _$10 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
circle(280, 280, 33);
    }
}
class __7 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
    }
}
class _$11 {
    constructor() {
    }
    display() {
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(0, 0, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
rect(200, 200, 95.4, 79.5);
fill("#FFFFFF");
stroke("#000000");
circle(280, 280, 33);
fill("#FFFFFF");
stroke("#000000");
triangle(230, 275, 258, 220, 286, 275);
    }
}
