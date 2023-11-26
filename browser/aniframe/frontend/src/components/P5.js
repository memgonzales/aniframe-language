import React, { useState } from "react";

function P5() {

    /* default p5 code:
        function setup() {
            createCanvas(windowWidth, windowHeight);
        }
            
        function draw() {
            background(100, 100, 255);
        }
    */
    return (
        <div className="p5">
            <script type="text/p5" data-autoplay src="http://127.0.0.1:8080/static/sample.js" data-p5-version="1.8.0" data-height="1000" data-preview-width="1000">
            </script>
        </div>
    );
}

export default P5;