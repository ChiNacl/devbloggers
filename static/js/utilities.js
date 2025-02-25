/*
const stackElementContainer = document.querySelector('.js-stack-container');
const stackElement = document.querySelector('.js-stack');
let stackHTML = '';

stackElement.addEventListener('keypress', (event)=>{
    if (event.key === 'Enter') {
        stackHTML += `<p>${stackElement.value}</p>`;
        stackElementContainer.innerHTML = stackHTML; 
        stackElement.value = '';
    }
});
*/
// const stackElementContainer = document.querySelector('.js-stack-container');
// const stackElement = document.querySelector('.js-stac');

const element = document.querySelector('.js-choice');
const choices = new Choices(element, {
    removeItemButton: true,
    duplicateItemsAllowed: false,
});
