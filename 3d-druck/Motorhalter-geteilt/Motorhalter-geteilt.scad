// mm. Assembly: motor shaft +Z, front of motor at Z=0, floor Y=-51.5.
part="assembly";
$fn=96;
module ring(ro,ri,h){difference(){cylinder(r=ro,h=h);translate([0,0,-.1])cylinder(r=ri,h=h+.2);}}
module bolt_holes(z,h,countersink=false){for(a=[30,150,270])rotate([0,0,a])translate([18.5,0,z]){cylinder(d=3.2,h=h);if(countersink)translate([0,0,h-1.6])cylinder(d1=3.2,d2=6.4,h=1.61);}}
module sleeve(){
 difference(){
  union(){translate([0,0,-30.5])cylinder(d=29,h=32.5);cylinder(r=22.5,h=2);}
  translate([0,0,-30.6])cylinder(d=24.2,h=30.6);
  translate([0,0,-.1])cylinder(d=3.2,h=2.3);
  for(x=[-6,6])translate([x-1.5,-17,-30.6])cube([3,12,5]);
  translate([-.7,11,-30.6])cube([1.4,6,27.5]);
  bolt_holes(-.1,2.1,true);
 }
 for(a=[30,150,270])rotate([0,0,a])translate([12.2,0,-29.5])cylinder(r=.3,h=29,$fn=24);
}
module rear_grille(){
 difference(){
  union(){
   // All grille front faces at Z=0: print face down without support.
   translate([0,0,-4])ring(46,42,4);
   translate([0,0,-3])ring(25,14.6,3);
   for(a=[0:10:350])rotate([0,0,a])translate([24,-.75,-2])cube([20,1.5,2]);
   for(r=[29,39])translate([0,0,-2])ring(r+.75,r-.75,2);
   for(x=[-15,15])translate([x-4,-39,-6])cube([8,8,6]);
  }
  // Sleeve pilot 29 mm in a 29.2 mm bore; flange rests on front at Z=0.
  bolt_holes(-3.1,3.2);
  // Clearance for stand shoulders, including the surrounding circular rim.
  for(x=[-15,15])translate([x-4.1,-41.6,-7.1])cube([8.2,2.7,7.2]);
  // Stand sockets open at the lower edge. 3.8 x 2 mm tenons; +0.2 clearance.
  for(x=[-15,15])translate([x-2,-39.1,-4.1])cube([4,7.3,2.2]);
 }
}
module stand(){
 translate([-29,-51.5,-25])cube([58,3,45]);
 for(x=[-15,15]){
  translate([x-4,-49,-7])cube([8,10,2.8]);
  translate([x-4,-41.5,-7])cube([8,2.5,7]);
  translate([x-1.9,-39.05,-4])cube([3.8,7,2]);
 }
}
if(part=="sleeve")translate([0,0,2])rotate([180,0,0])sleeve();
if(part=="grille")rotate([180,0,0])rear_grille();
if(part=="stand")translate([0,0,51.5])rotate([90,0,0])stand();
if(part=="assembly"){color("teal")sleeve();color("silver")rear_grille();color("teal")stand();}
