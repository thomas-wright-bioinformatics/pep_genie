let count = 0;
let mouse = {
    x: 0,
    y: 0, 
    startX: 0,
    startY: 0
};
let drawn = false;
let seScaling = false;
let moving = false;
let gridDrawn = false;

let startHandleLeft = 0;
let startHandleTop = 0;
let startWidth = 0;
let startHeight = 0;
let startTop = 0;
let startLeft = 0;
const handleSe = document.getElementById("resize-handle-se");
const canvas = document.getElementById("align-canvas");
const grid = document.getElementById('grid-div');


function setMousePosition(e) {
    mouse.x = e.clientX-canvas.offsetLeft;
    mouse.y = e.clientY-canvas.offsetTop;   
};




function beginDrawing(canvas){
    

    canvas.onmousemove = function (e) {
        setMousePosition(e);
        if (gridDrawn) {
            grid.style.width = Math.abs(mouse.x - mouse.startX) + 'px';
            grid.style.height = Math.abs(mouse.y - mouse.startY) + 'px';
            grid.style.left = (mouse.x - mouse.startX < 0) ? mouse.x + 'px' : mouse.startX + 'px';
            grid.style.top = (mouse.y - mouse.startY < 0) ? mouse.y + 'px' : mouse.startY + 'px';
            handleSe.style.left = startHandleLeft + mouse.x - mouse.startX +'px';
            handleSe.style.top = startHandleTop + mouse.y - mouse.startY +'px';

        };
        if (seScaling) {
            grid.style.width = startWidth + mouse.x-mouse.startX +'px';
            grid.style.height = startHeight + mouse.y-mouse.startY +'px';
            console.log('se', mouse.y-mouse.startY)
            handleSe.style.left = startHandleLeft + mouse.x - mouse.startX +'px';
            handleSe.style.top = startHandleTop + mouse.y - mouse.startY + 'px';

        }
        if (moving) {
            grid.style.left = startLeft + (mouse.x - mouse.startX) + 'px';
            grid.style.top = startTop + (mouse.y - mouse.startY) +'px';
            let gridRect = grid.getBoundingClientRect();
            let canvasRect = canvas.getBoundingClientRect();
            console.log('moving', gridRect.top- canvasRect.top, gridRect.left-canvasRect.left)
            handleSe.style.left = startHandleLeft + mouse.x - mouse.startX +'px';
            handleSe.style.top = startHandleTop + mouse.y - mouse.startY +'px';
        }
    }


    canvas.onclick = function (e) {
        if (gridDrawn == true) {
            canvas.style.cursor = "default";
            count = 1;     /* Limit on how many rectangles can be drawn */
            gridDrawn = false;
        } else {
            if (count !== 1 && gridDrawn == false) {
                mouse.startX = mouse.x;
                mouse.startY = mouse.y;
                grid.style.display = 'block'
                grid.style.position = 'relative'
                grid.style.left = mouse.x + 'px';
                grid.style.top = mouse.y + 'px';
                canvas.appendChild(grid)
                canvas.style.cursor = "crosshair";

                handleSe.style = "display: block; position: absolute; width: 20px; height: 20px; background: rgba(0, 78, 97, 0.4); z-index: 999;"
                canvas.appendChild(handleSe);
                handleSe.style.left = canvas.offsetLeft + mouse.x + 'px';
                startHandleLeft = canvas.offsetLeft + mouse.x;
                handleSe.style.top = canvas.offsetTop + mouse.y + 'px';
                startHandleTop = canvas.offsetTop + mouse.y;

                gridDrawn = true;
            }
        }
    }

    handleSe.onmousedown = function(e) {
        if (count == 1) {
            seScaling = true;
            startWidth = parseInt(grid.style.width,10);
            startHeight = parseInt(grid.style.height,10);
            startHandleTop = parseInt(handleSe.style.top,10)
            startHandleLeft = parseInt(handleSe.style.left,10)
            mouse.startX = mouse.x
            mouse.startY = mouse.y
        }
    }

    grid.onmousedown = function (e) {
        if (count == 1) {
            mouse.startX = mouse.x
            mouse.startY = mouse.y
            startLeft = parseInt(grid.style.left,10);
            startTop = parseInt(grid.style.top,10);
            startHandleTop = parseInt(handleSe.style.top,10)
            startHandleLeft = parseInt(handleSe.style.left,10)
            moving = true;

        }
    }


    canvas.onmouseup = function(e) {
        if (count == 1) {
            seScaling = false;
            moving = false;
        }
    }
};


function saveCoordsSubmit() {  
    let grid = document.getElementById('grid-div');
    let gridRect = grid.getBoundingClientRect()
    let canvas = document.getElementById('align-canvas');
    let canvasRect = canvas.getBoundingClientRect()
    let btn = document.getElementById('align-submit');
    let x1 = (gridRect.left - canvasRect.left)/canvasRect.width;
    let y1 = (gridRect.top - canvasRect.top)/canvasRect.height;
    let x2 = (gridRect.right - canvasRect.left)/canvasRect.width;
    let y2 = (gridRect.bottom - canvasRect.top)/canvasRect.height;
    let canvas_width = canvasRect.width;
    let canvas_height = canvasRect.height;
    document.getElementById('coordX1').value = x1;
    document.getElementById('coordY1').value = y1;
    document.getElementById('coordX2').value = x2;
    document.getElementById('coordY2').value = y2;
    document.getElementById('canvas_width').value = canvas_width;
    document.getElementById('canvas_height').value = canvas_height;
}







