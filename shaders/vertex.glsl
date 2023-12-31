#version 330 core

// Location of the attributes
layout (location=0) in vec3 vertexPos; // Position
layout (location=1) in vec3 vertexColor; // Colors

out vec3 fragmentColor;

void main() {
    gl_Position = vec4(vertexPos, 1.0);
    fragmentColor = vertexColor;
}
