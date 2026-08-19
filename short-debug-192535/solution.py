// total is wrong
subtotal(cart)      // correct
applyDiscount(total) // correct
applyTax(total) {
  return (total * 1.08) * (1 - discount); // <- again
}
