import java.util.*;

public class BinarySearch
{ 
  public static int rank(int key, int[] a)
	{ int lo=0;
          int hi=a.length-1;
	  while(lo<=hi)
		{int mid=(lo+hi)/2;
		if (key<a[mid]) hi=mid-1;
		else if (key>a[mid]) lo=mid+1;
		else return mid;}
	return -1;}

  public static void main(String[] args){
        int key=14;
	int[] intArray={1,2,4,6,7,3,5,8};
	Arrays.sort(intArray);
	if (rank(key,intArray)<0) System.out.println("Hello World!");}
}
