import * as THREE from "three";
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// Set up scene, background, camera, and renderer
var scene = new THREE.Scene();
scene.background = new THREE.Color('gainsboro');

var camera = new THREE.PerspectiveCamera(30, innerWidth / innerHeight, 0.1, 1000);
camera.position.set(10, 10, 10);
camera.lookAt(scene.position);

var renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

var controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;

window.addEventListener("resize", () => {
    camera.aspect = innerWidth / innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth, innerHeight);
});

// // Add this in later to make it visually appealing
// var ambientLight = new THREE.AmbientLight('white', 0.5);
// scene.add(ambientLight);

// var light = new THREE.DirectionalLight('white', 0.5);
// light.position.set(1, 1, 1);
// scene.add(light);

function createColoredCube(color_top, color_bot, color_left, color_right, color_front, color_back, center) {
    var canvas = document.createElement('canvas');
    // our box is divided into 512 x 512 pixels, regardless of the true size
    canvas.width = 512;
    canvas.height = 512;

    var context = canvas.getContext('2d');
    context.fillStyle = 'white';
    context.fillRect(0, 0, 512, 512);
    context.strokeStyle = 'black';
    context.lineWidth = 32;
    context.strokeRect(16, 16, 512 - 32, 512 - 32);

    var colors = [color_right, color_left, color_top, color_bot, color_front, color_back];
    var materials = colors.map(color => new THREE.MeshBasicMaterial({ color: color, map: new THREE.CanvasTexture(canvas) }));

    // Box should be 1 x 1 x 1 so that if we have center @ (0, 0, 0) corners at (0, 0, +/-1), etc.
    var cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), materials);
    cube.position.set(center.x, center.y, center.z);

    return cube;
}

// Create our cube made up of 27 cubies (center is never actually seen)
for (var i = -1; i < 2; i++) {
    for (var j = -1; j < 2; j++) {
        for (var k = -1; k < 2; k++) {
            var cube = createColoredCube('white', 'yellow', 'green', 'blue', 'red', 'orange', new THREE.Vector3(i, j, k));
            scene.add(cube);
        }
    }
}

function animationLoop() {
    controls.update();
    renderer.render(scene, camera);
}

renderer.setAnimationLoop(animationLoop);
