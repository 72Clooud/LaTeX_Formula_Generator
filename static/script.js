const btn = document.querySelector('.copy');
btn.addEventListener('click', () => {
    const formulaElement = document.querySelector('#latexFormula');
    
    if (formulaElement) {
        const formulaText = formulaElement.getAttribute('data-latex');
        copyToClipboard(formulaText)
    }
});

function copyToClipboard(txt) {
    navigator.clipboard.writeText(txt)
}