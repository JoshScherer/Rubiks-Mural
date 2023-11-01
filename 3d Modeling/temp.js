import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.126.1/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.126.1/examples/jsm/controls/OrbitControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);

const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(50, 50, 50);
scene.add(directionalLight);

camera.position.z = 5;

function createFace(color) {
  const size = 0.95; // Adjusted size to create gaps
  const geometry = new THREE.BoxGeometry(size, size, size);
  const material = new THREE.MeshLambertMaterial({ color: color });
  return new THREE.Mesh(geometry, material);
}

function createCubeFace(color, position, rotation) {
  const group = new THREE.Group();

  const offset = 1; // Distance between the centers of two adjacent cubies
  for (let x = -offset; x <= offset; x += offset) {
      for (let y = -offset; y <= offset; y += offset) {
          const cube = createFace(color);
          cube.position.set(x, y, 0);
          group.add(cube);
      }
  }

  group.position.copy(position);
  group.rotation.copy(rotation);
  return group;
}

const cubeSize = 3;
const colors = ['red', 'green', 'blue', 'yellow', 'white', 'orange'];
const positions = [
  new THREE.Vector3(0, 0, cubeSize / 2),  // front
  new THREE.Vector3(0, 0, -cubeSize / 2), // back
  new THREE.Vector3(cubeSize / 2, 0, 0),  // right
  new THREE.Vector3(-cubeSize / 2, 0, 0), // left
  new THREE.Vector3(0, cubeSize / 2, 0),  // top
  new THREE.Vector3(0, -cubeSize / 2, 0), // bottom
];

const rotations = [
  new THREE.Euler(0, 0, 0),            // front
  new THREE.Euler(0, Math.PI, 0),      // back
  new THREE.Euler(0, Math.PI / 2, 0),  // right
  new THREE.Euler(0, -Math.PI / 2, 0), // left
  new THREE.Euler(-Math.PI / 2, 0, 0), // top
  new THREE.Euler(Math.PI / 2, 0, 0),  // bottom
];

for (let i = 0; i < colors.length; i++) {
  const face = createCubeFace(colors[i], positions[i], rotations[i]);
  scene.add(face);
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

animate();
