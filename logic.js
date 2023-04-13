
var waveAmount = 3;
var unit1={life:5,position:0,type:1,loot:50},unit2={life:10,position:0,type:2,loot:150},unit3={life:25,position:0,type:3,loot:500};
var waves = [];
var waveindexNumber = 0;
var waveTimer;
var lives = 5;
var money = 200;//used to buy towers
var lanes = [[],[],[],[],[]];//the lanes on the gamefield
// unit = {life,position,type};
var tower = "";
var rook = {name:"Rook",health:3,lane:0,position:0,type:1,attack:1,atkSpeed:2,cost:200,note:"Attacks all enemies in it's lane"};
var bishop = {name:"Bishop",health:3,lane:0,position:0,type:2,attack:2,atkSpeed:1.4,cost:100,note:"Attacks the first enemies in the lanes next to it"};
var pawn = {name:"Pawn",health:3,lane:0,position:0,type:3,attack:2,atkSpeed:1.2,cost:50,note:"Attacks the first enemy in it's lane"};
var wall = {name:"Wall",health:15,lane:0,position:0,type:4,attack:0,cost:100,note:"Do not attack but have high health"};
var towers = [];
var paused = true;
var endOfLanes = 1001;
var pattern1 = [3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4];
var tileSelected = [];
// -------------------------------------------
var gameCanvas,c;
var tileWidth=100;
var tileHeight=50;
var tileOffsX=0;
var tileOffsY=0;
var tileLean=tileWidth/tileHeight;
var mx,my;          
// Current Hover Tile
var hx=0,hy=0,mx=0,my=0;          
// Tilemap
var tiles=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]];
function init2DGraphics()
{  
    gameCanvas = document.getElementById("gameWindow");
    c=gameCanvas.getContext("2d");                                             
}
function drawBox(x,y,strokecolor,fillcolor){
    c.save();
    c.translate(x,y);

    c.strokeStyle = strokecolor;
    c.fillStyle = fillcolor;
    c.lineWidth = 1.5;
    
    c.globalAlpha = 0.5;
    c.beginPath();
    c.moveTo(0,0);
    c.lineTo(100,0);
    c.lineTo(100,50);
    c.lineTo(0,50);
    c.closePath();
    
    if(fillcolor!="") {
        c.fill()
    };
    if(strokecolor!="") {
        c.stroke();
    }

    c.restore();            
}
function pointerCircle() {
    c.save();

    c.strokeStyle = "black";
    c.fillStyle = "blue";
    c.lineWidth = 1.5;
    
    c.globalAlpha = 1.0;
    c.beginPath();
    c.arc(mx, my, 6, 0, ((Math.PI/180)*360), true); 
    c.closePath();
    
    c.fill();
    c.stroke();

    c.restore();          
    
}
function drawUnit(u,lane) {
    c.save();
    switch (u.type) {
        case 1:
            c.fillStyle = "#00ff00";
            break;
        case 2:
            c.fillStyle = "#00ff00";
            break;
        case 3:
            c.fillStyle = "#00ff00";
            break;            
        default:
            c.fillStyle = "#000000";
            break;
    }
    
    c.strokeStyle = "black";
    c.lineWidth = 1.5;

    ypos = 50*lane-5;
    c.globalAlpha = 1.0;
    c.beginPath();
    c.rect(u.position, ypos,u.life*10,10);
    c.closePath();
    
    c.fill();
    c.stroke();

    c.restore();            
}    
function display(){
    c.clearRect(0, 0, 1000, 500);
    for(cy=0;cy<5;cy++){
        for(cx=0;cx<10;cx++){
            if(tiles[cx][cy]==1){
                drawBox(tileOffsX+(tileWidth)*cx,tileOffsY+(cy*tileHeight),"#444","blue");
            }
            else if(tiles[cx][cy]==2){
                drawBox(tileOffsX+(tileWidth)*cx,tileOffsY+(cy*tileHeight),"#444","green");
            }
            else if(tiles[cx][cy]==3){
                drawBox(tileOffsX+(tileWidth)*cx,tileOffsY+(cy*tileHeight),"#444","red");
            }
            else if(tiles[cx][cy]==4){
                drawBox(tileOffsX+(tileWidth)*cx,tileOffsY+(cy*tileHeight),"#444","purple");
            }
            else if(mx >= tileWidth*cx && mx <= tileWidth*(cx+1) && my >= tileOffsY+(tileHeight*(cy)) && my <= tileOffsY+(tileHeight*(cy+1)) ){
                drawBox(tileOffsX+(tileWidth)*cx,tileOffsY+(cy*tileHeight),"#444","#222");
            }
            else if(tiles[cx][cy]==0){
                //sdrawBox(tileOffsX+(tileWidth)*cx,tileOffsY+(cy*tileHeight),"#444","white");
            }
            if(cx == tileSelected[0] && cy == tileSelected[1]){
                drawBox(tileOffsX+(tileWidth)*cx,tileOffsY+(cy*tileHeight),"#444","lightgrey");
            }
        }
    }
    for (let i = 0; i < lanes.length; i++) {
        var laneNr = lanes[i];
        for (let j = 0; j < laneNr.length; j++) {
            var laneUnit = laneNr[j];
            drawUnit(laneUnit,i);
        }                
    }
    pointerCircle();
    
}
function selectTile(){
    for(cy=0;cy<5;cy++){
        for(cx=0;cx<10;cx++){
            if(mx >= tileWidth*cx && mx <= tileWidth*(cx+1) && my >= tileOffsY+(tileHeight*(cy)) && my <= tileOffsY+(tileHeight*(cy+1)) ){
                if (tiles[cx][cy] == 0 && tower != "") {
                    placeTower(tower,cy+1,cx+1);
                } else if (tiles[cx][cy] != 0) {
                    tileSelected[0] = cx;
                    tileSelected[1] = cy;
                    console.log(tileSelected);
                }
            }
        }
    }
}
//------------------------------------------2d graphics end
function mouseMove(e,t){        
    var rect = e.target.getBoundingClientRect();
    mx = e.clientX - rect.left; //x position within the element.
    my = e.clientY - rect.top;  //y position within the element.
}
function restartGame(){
    paused = true;
    waves = [];
    waveindexNumber=0;
    towers = [];
    lanes = [[],[],[],[],[]];
    for (let i = 0; i < 3; i++) {
        waves[i]=[];
        count=1;
        for (let index = 0; index < 10; index++) {
            waves[i].push({spawnTime:count*300,lane:pattern1[index],unit:{life:5,position:0,type:1,loot:50}})
            count++;            
        }            
    }
    lives = 5;
    money = 200;
    document.getElementById("lifeCounter").innerHTML = "lives: " + lives;
    document.getElementById("moneyCounter").innerHTML = "Cash: " + money;
    //clearField();
}
function spawnUnit(lane,unit){
    lanes[lane].push(unit);
}

function placeTower(tower,l,pos){
    if (money>=tower.cost) {
        tiles[pos-1][l-1] = tower.type;
        console.log(tiles[pos-1][l-1]);
        var t = {name:tower.name,health:tower.health,lane:l,position:pos,type:tower.type,attack:tower.attack,atkSpeed:tower.atkSpeed,cost:tower.cost,note:tower.note};
        towers.push(t);
        money=money - tower.cost;
    }

}

function selectTower(t){
    tower=t;
}

setInterval(() => {
    document.getElementById("lifeCounter").innerHTML = "lives: " + lives;
    document.getElementById("moneyCounter").innerHTML = "Cash: " + money;
    gameLoop();
}, 5);

function nextWave(){
    waveindexNumber++;
    waveTimer=0;
    paused=false;
    document.getElementById("nextWaveButton").setAttribute("disabled",true);
}

function gameLoop(){
    display();
    if (!paused && waveindexNumber <= waveAmount) {
        activeWave(waves[waveindexNumber-1]);     
    }
}

function activeWave(wave){
    waveTimer++;
    //enemy spawn
    for (let i = 0; i < wave.length; i++) {
        if (wave[i].spawnTime==waveTimer) {
            spawnUnit(wave[i].lane,wave[i].unit);
        }
    }
    //Enemy unit movement
    for (let i = 0; i < lanes.length; i++) {                
        var dead=[];
        for (let j = 0; j < lanes[i].length; j++) {
            var attacked=false;
            for (let k = 0; k < towers.length; k++) {
                if (lanes[i][j].position==towers[k].position*100-101 && i == towers[k].lane) {
                        attacked=true;
                    if (waveTimer%200 == 0) {
                        towers[k].health--;
                        if (towers[k].health == 0) {
                            console.log(towers[k].position-1)
                            console.log(towers[k].lane-1)
                            tiles[towers[k].position-1][towers[k].lane-1] = 0;
                            towers.splice(k,1);
                        }
                    }
                }
            }
            if (!attacked){
                lanes[i][j].position++;
                if (lanes[i][j].position==endOfLanes) {
                    lives--;
                    document.getElementById("lifeCounter").innerHTML = lives;
                    dead.push([i,j]);
                }
            }
        }
        for (let j = 0; j < dead.length; j++) {
            lanes[dead[j][0]].splice(dead[j][1],1);
        }
        
    }
    //tower attacks
    for (let i = 0; i < towers.length; i++) {
        var t = towers[i];
        if (t.type==1) {//rook
            var dead=[];
            for (let j = 0; j < lanes[t.lane].length; j++) {
                if (waveTimer%(t.atkSpeed*200) == 0) {
                    lanes[t.lane][j].life = lanes[t.lane][j].life - t.attack;
                }
                if(lanes[t.lane][j].life <= 0) {
                    dead.push(j);
                }
            }
            for (let j = 0; j < dead.length; j++) {
                money = money+lanes[t.lane][dead[j]].loot;
                lanes[t.lane].splice(dead[j],1);                    
            }
        } else if (t.type==2) {//bishop
            if (lanes[t.lane+1]) {
                if (lanes[t.lane+1] .length>= 1) {
                    if (waveTimer%(t.atkSpeed*200) == 0) {
                        lanes[t.lane+1][0].life = lanes[t.lane+1][0].life - t.attack;
                    }
                    if (lanes[t.lane+1][0].life <= 0) {
                        money = money+lanes[t.lane+1][0].loot;
                        lanes[t.lane+1].shift();
                    }
                }
            }
            if (lanes[t.lane-1]) {
                if (lanes[t.lane-1].length >= 1) {                            
                    if (waveTimer%(t.atkSpeed*200) == 0) {
                        lanes[t.lane-1][0].life = lanes[t.lane-1][0].life - t.attack;
                    }
                    if (lanes[t.lane-1][0].life <= 0) {
                        money = money+lanes[t.lane-1][0].loot;
                        lanes[t.lane-1].shift();
                    }
                }   
            }
                                
        } else if (t.type==3) {//pawn
            console.log(t.lane);
            if (lanes[t.lane].length >= 1) {     
                if (waveTimer%(t.atkSpeed*200) == 0) {
                    lanes[t.lane][0].life = lanes[t.lane][0].life - t.attack;
                }
                if (lanes[t.lane][0].life <= 0) {
                    money = money+lanes[t.lane][0].loot;
                    lanes[t.lane].shift();
                }
            }               
        }
        
    }
    //lose condition
    if (lives<=0) {
        if (confirm("Play again?")) {
            restartGame();
        }
    }
    //end of wave condition
    
    if (wave[wave.length-1].spawnTime  < waveTimer && lanes[0].length == 0 && lanes[1].length == 0 && lanes[2].length == 0 && lanes[3].length == 0 && lanes[4].length == 0) {
        console.log(lanes);
        paused=true;
        document.getElementById("nextWaveButton").removeAttribute("disabled");
        for (let index = 0; index < towers.length; index++) {
            var t = towers[index];                 
        }
    }

}