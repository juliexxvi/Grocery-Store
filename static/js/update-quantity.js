for (let i = 0; i < 36; i++) {
  const minusButton = document.querySelector(`#minus-${i}`);
  const plusButton = document.querySelector(`#plus-${i}`);
  const quantityEle = document.querySelector(`#quantity-${i}`);
  let quantity = Number(quantityEle.value);

  minusButton.addEventListener("click", () => {
    if (quantity == 0) {
      return;
    }
    quantity--;
    quantityEle.value = quantity;
  });
  plusButton.addEventListener("click", () => {
    quantity++;
    quantityEle.value = quantity;
  });
}
