function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData('text', event.target.id);
}

function drop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData('text');
    const element = document.getElementById(data);

    if (event.target.id === 'dropzone' || event.target.parentNode.id === 'dropzone') {
        
        element.style.width = '120px';
        element.style.height = '120px';
        event.target.appendChild(element);
    }
}

document.getElementById('check-order').addEventListener('click', function () {
    const dropzone = document.getElementById('dropzone');
    const children = Array.from(dropzone.getElementsByTagName('img'));
    const correctOrder = ['drag1', 'drag2', 'drag3', 'drag4', 'drag5'];

    const userOrder = children.map((child) => child.id);

    if (JSON.stringify(userOrder) === JSON.stringify(correctOrder)) {
        document.getElementById('feedback').innerText = 'Great job! The order is correct.';
        document.getElementById('feedback').style.color = 'green';
    } else {
        document.getElementById('feedback').innerText = 'Try again! The order is incorrect.';
        document.getElementById('feedback').style.color = 'red';
    }
});

document.getElementById('reset').addEventListener('click', function () {
    const dragContainer = document.getElementById('drag-container');
    const dropzone = document.getElementById('dropzone');
    const images = dropzone.getElementsByTagName('img');

    while (images.length > 0) {
        dragContainer.appendChild(images[0]);
    }

    document.getElementById('feedback').innerText = '';
});
