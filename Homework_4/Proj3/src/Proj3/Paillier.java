package Proj3;
import java.math.*;
import java.util.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Paillier 
{

//	p and q are two large primes.
//	lambda = lcm(p-1, q-1) = (p-1)*(q-1)/gcd(p-1, q-1).
	private BigInteger p, q, lambda;
	

//	n = p*q, where p and q are two large primes.
	public BigInteger n;
	

//	nsquare = n*n
	public BigInteger nsquare;
	

//	a random integer in Z*_{n^2} where gcd (L(g^lambda mod n^2), n) = 1.
	private BigInteger g;
	

//	number of bits of modulus
	private int bitLength;
	
	

//	Constructs an instance of the Paillier cryptosystem.
//	bitLengthVal number of bits of modulus
//	certainty The probability that the new BigInteger represents a prime number will exceed (1 - 2^(-certainty)). The execution time of this constructor is proportional to the value of this parameter.
	public Paillier(int bitLengthVal, int certainty) 
	{
		KeyGeneration(bitLengthVal, certainty);
	}
	
//	This function Writes Data to the Files
	public static void WriteToFile(String fileName, String[] array)
	{
		File fout = new File(fileName); // File Object
		FileOutputStream fos = null; // Clearing the output stream by setting it to null
		try {
			fos = new FileOutputStream(fout);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos)); //BufferedWriter Object creation
		
    	
//    	This Block of code will write the values of the array to the file
		try 
		{
			for (int i = 0; i < array.length; i++)
			{
				bw.write(array[i].toString());
				bw.newLine();
			}
			bw.close(); // Closing file to avoid file corruptions
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
	}

//	Constructs an instance of the Paillier cryptosystem with 512 bits of modulus and at least 1-2^(-64) certainty of primes generation.
	public Paillier() 
	{
		Scanner s1 = new Scanner(System.in);
		System.out.print("Enter key size:");
		int keySize = s1.nextInt();
		KeyGeneration(keySize, 64);
	}
	
	public void KeyGeneration(int bitLengthVal, int certainty) 
	{
		bitLength = bitLengthVal;
//		Constructs two randomly generated positive BigIntegers that are probably prime, with the specified bitLength and certainty.*/
		p = new BigInteger(bitLength / 2, certainty, new Random());
		q = new BigInteger(bitLength / 2, certainty, new Random());
		
		n = p.multiply(q);
		nsquare = n.multiply(n);
		Random r = new Random(); // Random Number Generator for the G Value!
		
		g = new BigInteger(Integer.toString(r.nextInt()));
		
		
		lambda = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE)).divide(
		p.subtract(BigInteger.ONE).gcd(q.subtract(BigInteger.ONE)));
		
		
//		check whether g is good.
		if (g.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).gcd(n).intValue() != 1) 
		{
			System.out.println("g is not good. Choose g again.");
			System.exit(1);
		}
			
		BigInteger u = g.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).modInverse(n);
		
//		Creating data to write to file
		String textP = "P = "+ p + " ";
		String textQ = "\nQ = "+ q + " ";
		String textG = "\nG = "+ g + " ";
		
//		Scanner object to read data from console
    	Scanner f1 = new Scanner(System.in);
    	System.out.println("Enter the filename for P, Q, G");
    	
    	String fileName = f1.next() + ".txt";    	
    	
    	String[] pqg = new String[3];
    	pqg[0] = textP;
    	pqg[1] = textQ;
    	pqg[2] = textG;
    	
    	WriteToFile(fileName, pqg); // Writing P, Q, G to the file!

    	
		String textLambda = "Lambda = " + lambda.toString();
		String textMu = "Mu = " + u.toString();
		System.out.println("Enter the filename for Lamda and Mu");
    	String fileName2 = f1.next() + ".txt";
    	
    	String[] lambda_mu = new String[2];
    	lambda_mu[0] = textLambda;
    	lambda_mu[1] = textMu;
    	
    	WriteToFile(fileName2, lambda_mu); // Writing Lambda and Mu to the file!
				
	}
	

//	Encrypts plaintext m. ciphertext c = g^m * r^n mod n^2. This function explicitly requires random input r to help with encryption.
//	m plaintext as a BigInteger
//	r random plaintext to help with encryption
//	returns the ciphertext as a BigInteger
	public BigInteger Encryption(BigInteger m, BigInteger r) 
	{
		return g.modPow(m, nsquare).multiply(r.modPow(n, nsquare)).mod(nsquare);	
	}
	

//	Encrypts plaintext m. ciphertext c = g^m * r^n mod n^2. This function automatically generates random input r (to help with encryption).
//	m plaintext as a BigInteger
//	returns the ciphertext as a BigInteger
	public BigInteger Encryption(BigInteger m) 
	{
		BigInteger r = new BigInteger(bitLength, new Random());
		return g.modPow(m, nsquare).multiply(r.modPow(n, nsquare)).mod(nsquare);	
	}
	
//	Decrypts ciphertext c. plaintext m = L(c^lambda mod n^2) * u mod n, where u = (L(g^lambda mod n^2))^(-1) mod n.
//	c ciphertext as a BigInteger
//	returns plaintext as a BigInteger
	public BigInteger Decryption(BigInteger c) 
	{
		BigInteger u = g.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).modInverse(n);
		return c.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).multiply(u).mod(n);
	}
	
	
	public static void main(String[] str) 
	{
//		instantiating an object of Paillier cryptosystem
		Paillier paillier = new Paillier();		
		int size; // Gets the size of the vectors from the console
//		Scanner obj to read from console!
		Scanner f1 = new Scanner(System.in);
		
		System.out.println("Enter the vector size");
		size = f1.nextInt();	
		
//		Creating different BigInteger arrays to store the values and encrypted values of U and V respectively
		BigInteger A[]= new BigInteger [size];
		BigInteger EA[]= new BigInteger [size];
		BigInteger EB[]= new BigInteger [size];
		BigInteger B[]= new BigInteger [size];
		String VecA[] = new String[size];
		String VecB[] = new String[size];
		BigInteger PowEA[]= new BigInteger [size];		
		BigInteger prod = new BigInteger("1");
		
		
		
		System.out.println("Enter the filename for Vector U");
    	String VecA_File = f1.next() + ".txt";
		System.out.println("Enter all the values of Vector U");
		
//		Loop that reads the bigInteger and creates a string copy of that bigInteger!
		for (int i=0; i<size;i++)
		{
			A[i]=f1.nextBigInteger();
			VecA[i] = "U[" + Integer.toString(i) + "] = " +  A[i].toString();
		}
		    	
		WriteToFile(VecA_File, VecA); // Writing Vector A to the file!
		
		System.out.println("Enter the filename for Vector V");
    	String VecB_File = f1.next() + ".txt";
		System.out.println("Enter all the values of Vector V");
		
//		Loop that reads the bigInteger and creates a string copy of that bigInteger!
		for (int i=0; i<size;i++)
		{
			B[i]=f1.nextBigInteger();
			VecB[i] = "V[" + Integer.toString(i) + "] = " + B[i].toString();
		}
		
		WriteToFile(VecB_File, VecB); // Writing Vector B to the file!    		
		
		System.out.println("Enter the filename for Encrypted U");
    	String EA_File = f1.next() + ".txt";
		String EA_Array[] = new String[size];
		
		//Multiplication of two vectors
		for (int i=0; i<size;i++)
		{
			EA[i] = paillier.Encryption(A[i]);
			EA_Array[i] = "EU[" + Integer.toString(i) + "] = " + EA[i].toString();
		}
		
		WriteToFile(EA_File, EA_Array); // Writing Vector EA to the file!		
		
		System.out.println("Enter the filename for Encrypted V");
    	String EB_File = f1.next() + ".txt";
		String EB_Array[] = new String[size];

		for (int i=0; i<size;i++)
		{
			EB[i] = paillier.Encryption(B[i]);
			EB_Array[i] = "EV[" + Integer.toString(i) + "] = " + EB[i].toString();
		}
		
		WriteToFile(EB_File, EB_Array); // Writing Vector EB to the file!				

		for (int i=0; i<size;i++)
		{
			BigInteger pow=EA[i].modPow(B[i], paillier.nsquare);
			PowEA[i] = pow;
			prod=prod.multiply(pow).mod(paillier.nsquare);		
		}
		
		System.out.println("Enter the filename for Encrypted DotProduct of U and V");
    	String EAB_File = f1.next() + ".txt";
		
    	File foutEAB = new File(EAB_File);
    	FileOutputStream fosEAB = null;
		try {
			fosEAB = new FileOutputStream(foutEAB);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bwEAB = new BufferedWriter(new OutputStreamWriter(fosEAB));
		
		try 
		{
			for (int i = 0; i < PowEA.length; i++)
			{
				bwEAB.write("E(U[" + Integer.toString(i) + "]" + ".V[" + Integer.toString(i) + "]) = " + PowEA[i].toString());
				bwEAB.newLine();
			}
			bwEAB.newLine();
			bwEAB.write("Final Dot Product = " + paillier.Decryption(prod).toString());
			bwEAB.close();


		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
		
		System.out.println("\n\n");
		System.out.println("Product = " + paillier.Decryption(prod).toString()); // Final Result
		
		System.out.println("All Files are now ready in the Project Folder!");
	}
}
