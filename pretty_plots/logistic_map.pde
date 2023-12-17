
float x = 0;
float xh = 0, xl = 1;
float rl = 3.5, rh = 3.7;
float r = rl;


void setup() {
  size(800, 1000);
  background(0);
  stroke(250, 5);
}

void draw() {
  r += (rh-rl)/width;
  for (int i=0; i<10000; i++)  {
    //print(x);
    x = r * x * (1-x);
    point(map(r, rl, rh, 0, width), map(x, xl, xh, height, 0));
    
  }
  if (r>rh) {
    //saveFrame("arb.png");
    noLoop();
  }
  x = 0.5;
}
