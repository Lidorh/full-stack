function bubbleSort(arr: number[]): void {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        }
      }
    }
  }
  
  // Example usage:
  const arr: number[] = [64, 25, 12, 22, 11];
  bubbleSort(arr);
  console.log("Sorted array:", arr);
  
  export {};
  // [1 , 5 , 2 , 3 , 4  , 7 , 8 , 10]
  // --> 9  , 6 