import * as THREE from "three";
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

var scene = new THREE.Scene();
scene.background = new THREE.Color('gainsboro');

var camera = new THREE.PerspectiveCamera(30, innerWidth / innerHeight);
camera.position.set(0, 0, 10);
camera.lookAt(scene.position);

var renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
renderer.setAnimationLoop(animationLoop);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
controls.dampingFactor = 0.25;


window.addEventListener("resize", () => {
    camera.aspect = innerWidth / innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(innerWidth, innerHeight);
});

var ambientLight = new THREE.AmbientLight('white', 0.5);
scene.add(ambientLight);

var light = new THREE.DirectionalLight('white', 0.5);
light.position.set(1, 1, 1);
scene.add(light);

var canvas = document.createElement('CANVAS');
canvas.width = 512;
canvas.height = 512;

var context = canvas.getContext('2d');
context.fillStyle = 'tan';
context.fillRect(0, 0, 512, 512);
context.strokeStyle = 'black';
context.lineWidth = 32;
context.strokeRect(16, 16, 512 - 32, 512 - 32);

// Array of colors for each face
var colors = [
    'red', 'green', 'blue', 'yellow', 'magenta', 'cyan'
];

// Create an array of materials with a different color for each face
var materials = colors.map(color => new THREE.MeshLambertMaterial({ color: color, map: new THREE.CanvasTexture(canvas) }));

var object = new THREE.Mesh(
    new THREE.BoxGeometry(2, 2, 2),
    materials
);
scene.add(object);

function animationLoop() {
    controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true
    renderer.render(scene, camera);
}

