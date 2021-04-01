/*
Extension 1: Add Sound
I've added sound functionality to make my game more interactive and addictive. I used multiple sounds for different functionalities which includes background sound, collect sound, victory sound, jump sound and falling sound. I downloaded these sounds from freemusic.com. I had difficulty adjusting sounds e.g after adding the background sound and the collectable collect sound I noticed whenever my character collects a coin the sound is not felt alot so I slightly increased the collectable collect sound volume for a better gaming experience. Also I increased the victory sound volume so whenever the game is won a winning atmosphere is felt with the help of the victory sound. I learnt about the wide p5.js sound library, it give different functionalities and one of them was the loop which I used to run the background music continuously while the game is being played.  

Extension 2: Create Enemies
I added enemies in my game to make it more difficult to play that eventually made the game more addictive. I added similar enemies at different positions. The game character needs to avoid coming in contact with the enemies or else it’ll lose its life. To stay safe the character needs to jump over the enemy. The enemy I’ve created is similar to my game character but its red colour body and greyish feet makes him different.I had difficulty using the constructor function at first and throughout the process of adding enemies I made quite a few syntax and logic errors which I then corrected by first trying my self, and If I couldn’t find the mistake I took help from videos. Although I had difficulty using constructor function but through this task I practiced it a lot. I also learnt how I can create different enemies at different positions to make the game tougher.
*/

/*
- Copy your game project code into this file
- for the p5.Sound library look here https://p5js.org/reference/#/libraries/p5.sound
- for finding cool sounds perhaps look here
https://freesound.org/
*/

var gameChar_x;
var gameChar_y;
var floorPos_y;
var scrollPos;
var gameChar_world_x;

var isLeft;
var isRight;
var isFalling;
var isPlummeting;

var trees_x;
var treePos_y;

var clouds;

var mountains;

var canyons;

var collectables;

var game_score;

var flagPole;

var lives;

var jumpSound;
var fallingSound;
var backgroundSound;
var collectSound;
var victorySound;

var enemies;

function preload()
{
    soundFormats('mp3','wav');
    
    //load your sounds here
    jumpSound = loadSound('assets/jump.wav');
    fallingSound = loadSound('assets/falling.wav');
    backgroundSound = loadSound('assets/background.mp3');  
    collectSound = loadSound('assets/collect.wav');
    victorySound = loadSound('assets/victory.mp3');

    jumpSound.setVolume(0.1);
    fallingSound.setVolume(0.1);
    backgroundSound.setVolume(0.1);
    collectSound.setVolume(0.15);
    victorySound.setVolume(0.3);
}


function setup()
{
	createCanvas(1024, 576);
    
	floorPos_y = height * 3/4;

    lives = 3;
    
    backgroundSound.loop()
    
    startGame()
}

function draw()
{
    
    // fill the sky blue
	background(100, 155, 255); 

    // draw some green ground
	noStroke();
	fill(0,155,0);
	rect(0, floorPos_y, width, height/4);
    
    //Start Scrolling
    push();
    translate(scrollPos,0); 
    
	// Draw clouds.
    drawClouds();

	// Draw mountains.
    drawMountains();

	// Draw trees.
    drawTrees();

	// Draw canyons.
    for (var i=0 ; i < canyons.length ; i++ )  
        {
            drawCanyon(canyons[i]);
            checkCanyon(canyons[i]);
        }
        
    
	// Draw collectable items.
    for (var i=0 ; i < collectables.length ; i++ ) 
        {
            if (!collectables[i].isFound)
                {
                    drawCollectable(collectables[i]);
                    checkCollectable(collectables[i]);
                }
        }
    
    //Call flagPole
    renderflagPole();
    
    //enemies draw
    for(var i=0; i < enemies.length; i ++)
        {
            enemies[i].draw();

            var isContact =
            enemies[i].checkContact(gameChar_world_x,gameChar_y);

                if(isContact)
                    {
                        if(lives > 0)
                            {
                                startGame();
                                lives -=1; 
                                break;
                            }          
                        else
                            {    
                                strokeWeight(5);
                                stroke(0);
                                fill(255);

                                textSize(60);    
                                text("Game Over!",width/2 - 200,height/2)

                                textSize(30);    
                                text("Press space to continue",width/2 - 200,height/2+ 40)
                                return;
                            }
                    }
        }
    
    
    //Call checkPlayerdie
    checkPlayerDie();
    

    //End Scrolling 
    pop();
    
	//Draw game character.
	drawGameChar();
    
    
    
    //Show Game Score
    stroke(255,215,0)
    strokeWeight(3)
    fill(0);
    rect(20,10,67,30)
    noFill();
    fill(255,215,0);
    noStroke()
    textSize(12);
    text("Score: " + game_score,30,30);
    noFill();
    
    
    //Remaining Lives
    fill(0);
    textSize(20);
    text("Lives: ",width-150,30);
    noFill();
    
    for ( var x=lives ; x>0 ; x--)
        
    {    
        if (x > 2)
            {    
                stroke(0,0,0)
                strokeWeight(3)
                fill (255,0,0)
                ellipse (width - 80  , 25 ,20)
                ellipse (width - 55  , 25 ,20)
                ellipse (width - 30  , 25 ,20)
            }  

        if (x > 1)
            {    
                stroke(0,0,0)
                strokeWeight(3)
                fill (255,0,0)
                ellipse (width - 80  , 25 ,20)
                ellipse (width - 55  , 25 ,20)
            }  

        if (x > 0)
            {    
                stroke(0,0,0)
                strokeWeight(3)
                fill (255,0,0)
                ellipse (width - 80  , 25 ,20)
            }          
    }
        
        
    //point 5
    if(lives < 1)
        {
            push();

            strokeWeight(5);
            stroke(0);
            fill(255);
            
            textSize(60);    
            text("Game Over!",width/2 - 200,height/2)

            textSize(30);    
            text("Press space to continue",width/2 - 200,height/2+ 40)
            return        
            pop();
        }
    
    if (flagPole.isReached == true)
        {
            strokeWeight(5);
            stroke(0);
            fill(255);
            
            textSize(60);    
            text("Level Complete",width/2 - 200,height/2)

            textSize(30);    
            text("Press space to continue",width/2 - 165,height/2+ 40)

            return 
        }
    
	// Logic to make the game character move or the background scroll.
	if(isLeft)
        {
            if(gameChar_x > width * 0.2)
                {
                    gameChar_x -= 5;
                }
            else
                {
                    scrollPos += 5;
                }
        }

	if(isRight)
        {
            if(gameChar_x < width * 0.8)
                {
                    gameChar_x  += 5;
                }
            else
                {
                    scrollPos -= 5; // negative for moving against the background
                }
        }
    
	// Logic to make the game character rise and fall.
    if (gameChar_y !== floorPos_y)
        {
            gameChar_y +=1;
            isPlummeting = true;     
        }
    else 
        {
            isPlummeting = false
        }    
    
    //Check flagPole
    if (flagPole.isReached == false)
        {
            checkflagPole();
        }
    
	// Update real position of gameChar for collision detection.
	gameChar_world_x = gameChar_x - scrollPos;
    

}

// ---------------------
// Key control functions
// ---------------------

function keyPressed()
{
    if (keyCode == 37)
        {
            console.log("left key")
            isLeft = true;
        }
    else if (keyCode == 39)
        {
            console.log("right key")
            isRight = true;
        }
    else if (keyCode == 32 && gameChar_y == floorPos_y)
        {
            console.log("space  bar")
            isPlummeting = true;
            gameChar_y = gameChar_y - 100;
            
            jumpSound.play();
        }    
}

function keyReleased()
{

    if (keyCode == 37)
        {
            console.log("left key")
            isLeft = false;
        }
    else if (keyCode == 39)
        {
            console.log("right key")
            isRight = false;
        }    

}

// ------------------------------
// Game character render function
// ------------------------------

// Function to draw the game character.
function drawGameChar()
{
    
    //jumping-left code
    if(isLeft && isFalling)
        {
            // Face
            fill(255, 182, 193);
            ellipse(gameChar_x ,gameChar_y-57 ,13,30);

            //Body
            fill(255,219,88);
            rect(gameChar_x-8 ,gameChar_y-42 ,15,35);

            //Feet
            fill(0)
            rect(gameChar_x-8 ,gameChar_y-7 ,5,10); 
            rect(gameChar_x+2 ,gameChar_y-7 ,5,10);  

            //Arms
            stroke(100);          
            line(gameChar_x-4,gameChar_y-30,gameChar_x+15 ,gameChar_y-55);
            line(gameChar_x+4,gameChar_y-30,gameChar_x+22,gameChar_y-50);        

        }
    
    //jumping-right code
    else if(isRight && isFalling)
        {
            // Face
            fill(255, 182, 193);
            ellipse(gameChar_x ,gameChar_y-57 ,13,30);

            //Body
            fill(255,219,88);
            rect(gameChar_x-8 ,gameChar_y-42 ,15,35);

            //Feet
            fill(0)
            rect(gameChar_x-8 ,gameChar_y-7 ,5,10); 
            rect(gameChar_x+2 ,gameChar_y-7 ,5,10);  

            //Arms
            stroke(100);      
            line(gameChar_x-4,gameChar_y-30,gameChar_x-22,gameChar_y-50);
            line(gameChar_x+4,gameChar_y-30,gameChar_x-15,gameChar_y-55);

        }
    
    //walking left code
    else if(isLeft)
        {
            // Face
            fill(255, 182, 193);
            ellipse(gameChar_x ,gameChar_y-57 ,13,30);

            //Body
            fill(255,219,88);
            rect(gameChar_x-8 ,gameChar_y-42 ,15,35);

            //Feet
            fill(0)
            rect(gameChar_x-8 ,gameChar_y-7 ,5,10); 
            rect(gameChar_x+2 ,gameChar_y-7 ,5,10);  

            //Arms
            stroke(100);
            line(gameChar_x-4,gameChar_y-30,gameChar_x-17,gameChar_y-25);
            line(gameChar_x+4,gameChar_y-30,gameChar_x-17,gameChar_y-20);    

        }
    
    //walking right code
    else if(isRight)
        {
            // Face
            fill(255, 182, 193);
            ellipse(gameChar_x ,gameChar_y-57 ,13,30);

            //Body
            fill(255,219,88);
            rect(gameChar_x-8 ,gameChar_y-42 ,15,35);

            //Feet
            fill(0)
            rect(gameChar_x-8 ,gameChar_y-7 ,5,10); 
            rect(gameChar_x+2 ,gameChar_y-7 ,5,10);  

            //Arms
            stroke(100);
            line(gameChar_x-4,gameChar_y-30,gameChar_x+17,gameChar_y-20);
            line(gameChar_x+4,gameChar_y-30,gameChar_x+17,gameChar_y-25);        


        }
    
    //jumping facing forwards code
    else if(isFalling || isPlummeting)
        {
            // Face
            fill(255, 182, 193);
            ellipse(gameChar_x ,gameChar_y-57 ,30,30);

            //Body
            fill(255,219,88);
            rect(gameChar_x-13 ,gameChar_y-42 ,25,35);

            //Feet
            fill(0)
            rect(gameChar_x-13 ,gameChar_y-7 ,10,10); 
            rect(gameChar_x+2 ,gameChar_y-7 ,10,10); 
            
            //Arms
            stroke(100);
            line(gameChar_x-9,gameChar_y-30,gameChar_x-22,gameChar_y-55);
            line(gameChar_x+9,gameChar_y-30,gameChar_x+22,gameChar_y-55);
        }
    
    //standing front facing code
    else
        {
            // Face
            fill(255, 182, 193);
            ellipse(gameChar_x ,gameChar_y-57 ,30,30);

            //Body
            fill(255,219,88);
            rect(gameChar_x-13 ,gameChar_y-42 ,25,35);

            //Feet
            fill(0)
            rect(gameChar_x-13 ,gameChar_y-7 ,10,10); 
            rect(gameChar_x+2 ,gameChar_y-7 ,10,10);  

            //Arms
            stroke(100);
            line(gameChar_x-9,gameChar_y-30,gameChar_x-19,gameChar_y-15);
            line(gameChar_x+9,gameChar_y-30,gameChar_x+19,gameChar_y-15);    
        }
}

// ---------------------------
// Background render functions
// ---------------------------

// Function to draw cloud objects.
function drawClouds ()
{
    // Draw clouds.
    for(var i=0 ; i < clouds.length ; i++)
        {
            fill(255);
            
            rect(clouds[i].x_pos,
                 clouds[i].y_pos,
                 80 * clouds[i].size,
                 30 * clouds[i].size);
            
             ellipse(clouds[i].x_pos,
                     clouds[i].y_pos + 5* clouds[i].size,
                     40* clouds[i].size,
                     50* clouds[i].size);
            
            ellipse(clouds[i].x_pos + 80* clouds[i].size,
                    clouds[i].y_pos + 5* clouds[i].size,
                    40* clouds[i].size,
                    50* clouds[i].size);
            
            ellipse(clouds[i].x_pos + 40 * clouds[i].size,
                    clouds[i].y_pos - 5,
                    70* clouds[i].size,
                    60* clouds[i].size);
        }
}

// Function to draw mountains objects.
function drawMountains()
{
 	// Draw mountains.
    for (var i=0 ; i < mountains.length ; i++ )
    
        {
            //Small mountain A
            fill(148,83,24);
            triangle(mountains[i].x_pos - 80 * mountains[i].size,
                     mountains[i].y_pos,
                     mountains[i].x_pos + 60 * mountains[i].size,
                     mountains[i].y_pos,
                     mountains[i].x_pos + 10,
                     mountains[i].y_pos - 300* mountains[i].size);

            //Big mountain A
            fill(148,83,24);    
            triangle(mountains[i].x_pos -   20* mountains[i].size,
                     mountains[i].y_pos,
                     mountains[i].x_pos + 180* mountains[i].size,
                     mountains[i].y_pos,
                     mountains[i].x_pos + 80* mountains[i].size,
                     mountains[i].y_pos - 350* mountains[i].size);
        }   
}

// Function to draw trees objects.
function drawTrees()
{
    for (var i=0 ; i < trees_x.length ; i++ )
        {  
            //Trunk 
            noStroke();
            fill(192,192,192,150);
            ellipse(trees_x[i]-15,treePos_y+160,120,25)
            fill(139,69,19);
            stroke(0);
            strokeWeight(3);
            rect(trees_x[i]-20,treePos_y+40,20,120,30);
            noStroke();

            //Leaves
            fill(40, 139, 34);
            ellipse(trees_x[i] - 10,treePos_y + 20,100,80); 
            ellipse(trees_x[i] - 40,treePos_y - 10,110,70);
            ellipse(trees_x[i] + 20,treePos_y - 10,110,70);
            ellipse(trees_x[i] - 10,treePos_y - 50,100,80); 

            //Fruits
            fill('red');
            stroke('black');
            strokeWeight(2);
            ellipse(trees_x[i] - 60, treePos_y - 10,10,10);
            ellipse(trees_x[i] + 20, treePos_y + 30,10,10);
            ellipse(trees_x[i], treePos_y- 50,10,10);
            ellipse(trees_x[i] - 30,treePos_y + 40,10,10);
            ellipse(trees_x[i] - 15,treePos_y- 10,10,10);
            ellipse(trees_x[i] + 40,treePos_y- 30,10,10);
            ellipse(trees_x[i] + 50,treePos_y,10,10);
            ellipse(trees_x[i] - 40,treePos_y- 60,10,10);
            noStroke();
        }
}

// ---------------------------------
// Canyon render and check functions
// ---------------------------------

// Function to draw canyon objects.
function drawCanyon(t_canyon)
{
    //Mud
    fill('#654321');
    triangle(t_canyon.x_pos,431,
             t_canyon.x_pos + t_canyon.width/2,580,
             t_canyon.x_pos + t_canyon.width,431);
    
    //Water
    fill('#83d7ee');   
    triangle(t_canyon.x_pos + 20,431,
             t_canyon.x_pos + t_canyon.width/2,550,
             t_canyon.x_pos + t_canyon.width -20,431);
}

// Function to check character is over a canyon.
function checkCanyon(t_canyon)
{  
        if (gameChar_world_x > t_canyon.x_pos &&
            gameChar_world_x < t_canyon.x_pos + t_canyon.width &&
            gameChar_y == floorPos_y) 
            {
                isPlummeting=true; 
                gameChar_y+=0.7;
                fallingSound.play();

            }   
}

// ----------------------------------
// Collectable items render and check functions
// ----------------------------------

// Function to draw collectable objects.
function drawCollectable(t_collectable)
{
    noStroke();
    fill(218,165,32);
    ellipse(t_collectable.x_pos,
            t_collectable.y_pos,
            60 * t_collectable.size,
            60 * t_collectable.size);
    
    //Small circle
    fill(255,215,0);
    ellipse(t_collectable.x_pos,
            t_collectable.y_pos,
            40 * t_collectable.size,
            40 * t_collectable.size);

   
    //Star
    fill(255);
    
    beginShape();
    
    vertex(t_collectable.x_pos - 20  * t_collectable.size,
           t_collectable.y_pos);
    
    vertex(t_collectable.x_pos - 5  * t_collectable.size,
           t_collectable.y_pos - 5 * t_collectable.size);
    
    vertex(t_collectable.x_pos,
           t_collectable.y_pos - 20 * t_collectable.size);
    
    vertex(t_collectable.x_pos + 5 * t_collectable.size,
           t_collectable.y_pos - 5 * t_collectable.size);
    
    vertex(t_collectable.x_pos + 20  * t_collectable.size,
           t_collectable.y_pos);
    
    vertex(t_collectable.x_pos + 5 * t_collectable.size,
           t_collectable.y_pos + 5 * t_collectable.size );
    
    vertex(t_collectable.x_pos,
           t_collectable.y_pos + 20  * t_collectable.size);
    
    vertex(t_collectable.x_pos - 5 * t_collectable.size,
           t_collectable.y_pos + 5 * t_collectable.size);
    
    endShape();
}

// Function to check character has collected an item.
function checkCollectable(t_collectable)
{
    
    if (dist(gameChar_world_x,gameChar_y,
             t_collectable.x_pos,t_collectable.y_pos) < 50)
        {
            t_collectable.isFound=true;
            game_score+=1;
            collectSound.play();
        };
}

function renderflagPole()
{
    push();
    strokeWeight(4)
    stroke(0);
    line(flagPole.pos_x,floorPos_y,flagPole.pos_x,floorPos_y-200)
    
    
    
    if(flagPole.isReached)
        {
            fill(255,0,0)
            rect(flagPole.pos_x,floorPos_y-200,75,50)

            strokeWeight(10)
            stroke(255)
            fill(0);
            textSize(10);
            text("Finish",flagPole.pos_x + 20,floorPos_y - 173);
        }
    else 
        {
            fill(255,0,0)
            rect(flagPole.pos_x,floorPos_y-60,75,50)

            strokeWeight(10)
            stroke(255)
            fill(0);
            textSize(10); text("Finish",flagPole.pos_x + 20,floorPos_y - 33);       
        }
    
    pop();
    
}

function checkflagPole()
{
    var d = abs(gameChar_world_x - flagPole.pos_x)
    
    if (d < 10)
        {
            flagPole.isReached=true;
            victorySound.play();
        }
}

function checkPlayerDie()
{
    if (gameChar_y > 576)
        {
            lives = lives - 1;
            
            if (lives < 4 && lives > 0)
            {
                startGame();
            }
            else
            {   
                lives=0; 
            }
        }
}

function startGame()
{
    game_score = 0;

	gameChar_x = width/2;
	gameChar_y = floorPos_y;    
    
	// Variable to control the background scrolling.
	scrollPos = 0;

	// Variable to store the real position of the gameChar in the game
	// world. Needed for collision detection.
	gameChar_world_x = gameChar_x - scrollPos;

	// Boolean variables to control the movement of the game character.
	isLeft = false;
	isRight = false;
	isFalling = false;
	isPlummeting = false;

	// Initialise arrays of scenery objects.
    trees_x= [-800,-965,-1400,-1580,0,-180,600,780,1140,1320,1850,2030,2210,3200];
    treePos_y=height/2    
    
    clouds = 
        [
            {x_pos: -250, y_pos: 110, size: 0.8},
            {x_pos: -660, y_pos: 70, size: 1},
            {x_pos: -1030, y_pos: 100, size: 1.2},
            {x_pos: -1400, y_pos: 110, size: 0.8},
            {x_pos: 1460, y_pos: 70, size: 1},        
            {x_pos: 50, y_pos: 110, size: 0.8},
            {x_pos: 360, y_pos: 70, size: 1},
            {x_pos: 730, y_pos: 100, size: 1.2},
            {x_pos: 1100, y_pos: 110, size: 0.8},
            {x_pos: 1460, y_pos: 70, size: 1},
            {x_pos: 1830, y_pos: 100, size: 1.2},
            {x_pos: 2200, y_pos: 110, size: 0.8},
            {x_pos: 2560, y_pos: 70, size: 1},
            {x_pos: 2930, y_pos: 100, size: 1.2},
            {x_pos: 3300, y_pos: 110, size: 0.8}       
        ]

    mountains = 
        [
            {x_pos: -475, y_pos: 435, size: 0.9},
            {x_pos: -1780, y_pos: 435, size: 0.7},      
            {x_pos: 175, y_pos: 435, size: 0.9},
            {x_pos: 1480, y_pos: 435, size: 0.7},
            {x_pos: 2500, y_pos: 435, size: 0.9},
            {x_pos: 3000, y_pos: 435, size: 0.7},        
         ]
    
    canyons = 
        [
            {x_pos:-710 , width:150},
            {x_pos:-1220 , width: 150},
            {x_pos:-2000 , width:150},        
            {x_pos:360 , width:150},
            {x_pos:870 , width: 150},
            {x_pos:1620 , width:150},
            {x_pos:2260 , width:150},
            {x_pos:2770 , width:150},
            {x_pos:3320 , width:150}          
        ]
    
    collectables = 
        [
            {x_pos: -480, y_pos: 400, size: 1},
            {x_pos: -900, y_pos: 400, size: 1},
            {x_pos: -1170, y_pos: 320, size: 1.25}, 
            {x_pos: -1500, y_pos: 400, size: 1},
            {x_pos: -1930, y_pos: 320, size: 1.25}, 
            {x_pos: 180, y_pos: 400, size: 1},
            {x_pos: 670, y_pos: 400, size: 1},
            {x_pos: 950, y_pos: 320, size: 1.25},   
            {x_pos: 1230, y_pos: 400, size: 1},
            {x_pos: 1390, y_pos: 400, size: 1},
            {x_pos: 1930, y_pos: 400, size: 1},
            {x_pos: 2110, y_pos: 400, size: 1},   
            {x_pos: 2700, y_pos: 400, size: 1},
            {x_pos: 3400, y_pos: 320, size: 1.25}
            ]



    flagPole = {isReached:false , pos_x: 3600}  
    
    enemies = [];

    enemies.push(new Enemy(100,floorPos_y,200));

    enemies.push(new Enemy(-300,floorPos_y,400));   

    enemies.push(new Enemy(1100,floorPos_y,200));

    enemies.push(new Enemy(1400,floorPos_y,200));  

    enemies.push(new Enemy(1900,floorPos_y,300));

    enemies.push(new Enemy(2500,floorPos_y,200));

    enemies.push(new Enemy(3000,floorPos_y,250));    
}

function Enemy(x,y,range)
    {
        this.x = x;
        this.y = y;
        this.range = range;

        this.currentX = x;
        this.inc = 1;

        this.update = function()
            {
                this.currentX += this.inc;

                if(this.currentX >= this.x + this.range)
                    {
                        this.inc -= 1;
                    }
                else if (this.currentX < this.x)
                    {
                        this.inc = 1;
                    }
            }
        
        this.draw = function()
            {
                this.update();

                // Face
                noStroke();
                fill(255, 182, 193);
                ellipse(this.currentX ,this.y-57 ,30,30);

                //Body
                fill(255,0,0);
                rect(this.currentX-13 ,this.y-42 ,25,35);

                //Feet
                fill(90)
                rect(this.currentX-13 ,this.y-7 ,10,10); 
                rect(this.currentX+2 ,this.y-7 ,10,10);  

                //Arms
                stroke(100);
                line(this.currentX-9,this.y-30,this.currentX-19,this.y-15);
                line(this.currentX+9,this.y-30,this.currentX+19,this.y-15);    

            }
            
            this.checkContact = function(gc_x,gc_y)
                {
                    var d = dist(gc_x,gc_y,this.currentX,this.y-10)
                        {
                            if(d < 30)
                                {
                                    return true;
                                }
                            else 
                                {
                                    return false;
                                }
                        }
        }
    }
