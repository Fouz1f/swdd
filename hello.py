//Fouz Alsharif 44412064

// Java code for linearly search x in arr[]. If x

// is present then return its location, otherwise

// return -1

class LinearSearch {

            // This function returns index of element x in arr[]

            static int search(int F[], int M, int x)

            {

                        for (int i = 0; i < M; i++) {

                                // Return the index of the element if the element

                                    // is found

                                    if (F[i] == x)

                                                return i;

                        }

 

                        // return -1 if the element is not found

                        return -1;

            }

 

            public static void main(String[] args)

            {

                        int[] F = { 3, 4, 1, 7, 5 };

                        int M = F.length;

                        int x = 4;

                        int index = search(F, M, x);

                        if (index == -1)

                          System.out.println("Element is not present in the array");

                        else

                          System.out.println("Element found at position " + index);

            }

}

//------------------------------------------------------------------------------------------------------