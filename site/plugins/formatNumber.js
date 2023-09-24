export default function (value) {
  if (typeof value !== 'number') {
    return value;
  }

  // Преобразование числа в строку, и разделение его на группы по 3 цифры с конца
  const numberString = value.toString();
  const parts = numberString.split('.');
  const integerPart = parts[0];
  const decimalPart = parts[1] || '';

  // Разделяем целую часть числа на группы по 3 цифры с конца и добавляем точки
  const formattedIntegerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, '.');

  const result = formattedIntegerPart + (decimalPart.length > 0 ? '.' + decimalPart : '');

  return result;
}
