let yourStacks = [];
let stacks = [];

document.querySelectorAll('.js-stack').forEach((stack) => {
    yourStacks.push(stack.innerHTML);
});

document.querySelectorAll('.js-stacks').forEach((stack) => {
    stacks.push(stack.innerHTML);
});

const element = document.querySelector('.js-choice');
const choices = new Choices(element, {
    choices: yourStacks,
    addChoices: true,
    removeItemButton: true,
    duplicateItemsAllowed: false,
});
 
let dropStack = [];
function stackDropdown () {
    stacks.forEach((stack) => {
        let stackObject = {};
        if (!yourStacks.includes(stack)) {
            stackObject.value = stack;
            stackObject.label = stack;
            dropStack.push(stackObject);
        }
    });
    return dropStack;
}

choices.setChoices(
    stackDropdown(),
    'value',
    'label',
    false,
);
