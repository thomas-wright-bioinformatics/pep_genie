/*
Copyright 2023, Thomas Wright

LICENSE NOTICE
This file is part of The Pep Genie.
The Pep Genie is free software: 
you can redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.
The Pep Genie is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with The Pep Genie.
If not, see <https://www.gnu.org/licenses/>. 
*/



/* mouse settings and objects */
let mouse = {
    x: 0,
    y: 0, 
    startX: 0,
    startY: 0
};

let seScaling = false;
let moving = false;
let gridDrawn = true;
let count = 1;

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
    
    /* when moving */
    canvas.onmousemove = function (e) {
        setMousePosition(e);
        
        if (seScaling) {
            grid.style.width = startWidth + mouse.x-mouse.startX +'px';
            grid.style.height = startHeight + mouse.y-mouse.startY +'px';
            console.log('se', mouse.y-mouse.startY)
            
            handleSe.style.left = startHandleLeft + mouse.x - mouse.startX +'px';
            handleSe.style.top = startHandleTop + mouse.y - mouse.startY + 'px';
            

        }
        if (moving) {
            console.log('start width', startLeft, startLeft + (mouse.x - mouse.startX) + 'px' )
            console.log('start t', startTop, startTop + (mouse.y - mouse.startY) +'px' )
            
            grid.style.left = startLeft + (mouse.x - mouse.startX) + 'px';
            grid.style.top = startTop + (mouse.y - mouse.startY) +'px';
            let gridRect = grid.getBoundingClientRect();
            let canvasRect = canvas.getBoundingClientRect();
            console.log('moving', gridRect.top- canvasRect.top, gridRect.left-canvasRect.left)
            /*
            handleSe.style.left = startHandleLeft + mouse.x - mouse.startX +'px';
            handleSe.style.top = startHandleTop + mouse.y - mouse.startY +'px';
            */
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
            console.log('mouse down on handle se')
            e.stopPropagation();
        }
    }

    grid.onmousedown = function (e) {
        if (count == 1) {
            console.log('mouse down on grid')
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







