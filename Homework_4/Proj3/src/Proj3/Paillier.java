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
	/**
	* p and q are two large primes.
	* lambda = lcm(p-1, q-1) = (p-1)*(q-1)/gcd(p-1, q-1).
	*/
	private BigInteger p, q, lambda;
	
	/**
	* n = p*q, where p and q are two large primes.
	*/
	public BigInteger n;
	
	/**
	* nsquare = n*n
	*/
	public BigInteger nsquare;
	
	/**
	* a random integer in Z*_{n^2} where gcd (L(g^lambda mod n^2), n) = 1.
	*/
	private BigInteger g;
	
	/**
	* number of bits of modulus
	*/
	private int bitLength;
	
	
	/**
	* Constructs an instance of the Paillier cryptosystem.
	* @param bitLengthVal number of bits of modulus
	* @param certainty The probability that the new BigInteger represents a prime number will exceed (1 - 2^(-certainty)). The execution time of this constructor is proportional to the value of this parameter.
	*/
	public Paillier(int bitLengthVal, int certainty) 
	{
		KeyGeneration(bitLengthVal, certainty);
	}
	
	
	/**
	* Constructs an instance of the Paillier cryptosystem with 512 bits of modulus and at least 1-2^(-64) certainty of primes generation.
	*/
	public Paillier() 
	{
		Scanner s1 = new Scanner(System.in);
		System.out.print("Enter key size:");
		int keySize = s1.nextInt();
		KeyGeneration(keySize, 64);
	}
	
	
	/**
	* Sets up the public key and private key.
	* @param bitLengthVal number of bits of modulus.
	* @param certainty The probability that the new BigInteger represents a prime number will exceed (1 - 2^(-certainty)). The execution time of this constructor is proportional to the value of this parameter.
	*/
	public void KeyGeneration(int bitLengthVal, int certainty) 
	{
		bitLength = bitLengthVal;
		/*Constructs two randomly generated positive BigIntegers that are probably prime, with the specified bitLength and certainty.*/
		p = new BigInteger(bitLength / 2, certainty, new Random());
		q = new BigInteger(bitLength / 2, certainty, new Random());
		
		n = p.multiply(q);
		nsquare = n.multiply(n);
		Random r = new Random();
		
		g = new BigInteger(Integer.toString(r.nextInt()));
		
		
		lambda = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE)).divide(
		p.subtract(BigInteger.ONE).gcd(q.subtract(BigInteger.ONE)));
		/* check whether g is good.*/
		if (g.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).gcd(n).intValue() != 1) 
		{
			System.out.println("g is not good. Choose g again.");
			System.exit(1);
		}
//		System.out.println(g);
		BigInteger u = g.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).modInverse(n);
		
		
		String textP = "P = "+ p + " ";
		String textQ = "\nQ = "+ q + " ";
		String textG = "\nG = "+ g + " ";
		String finalText = textP + textQ + textG;
    	Scanner f1 = new Scanner(System.in);
    	System.out.println("Enter the filename for P, Q, G");
    	String fileName = f1.next() + ".txt";
    	File fout = new File(fileName);
    	FileOutputStream fos = null;
		try {
			fos = new FileOutputStream(fout);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
		
		try 
		{
			bw.write(textP);
			bw.newLine();
			bw.write(textQ);
			bw.newLine();
			bw.write(textG);
			bw.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	Scanner f2 = new Scanner(System.in);
		String textLambda = "Lambda = " + lambda.toString();
		String textMu = "Mu = " + u.toString();
		System.out.println("Enter the filename for Lamda and Mu");
    	String fileName1 = f2.next() + ".txt";
    	File fout1 = new File(fileName1);
    	FileOutputStream fos1 = null;
		try {
			fos1 = new FileOutputStream(fout1);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bw1 = new BufferedWriter(new OutputStreamWriter(fos1));
		
		try 
		{
			bw1.write(textLambda);
			bw1.newLine();
			bw1.write(textMu);


			bw1.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
				
	}
	
	/**
	* Encrypts plaintext m. ciphertext c = g^m * r^n mod n^2. This function explicitly requires random input r to help with encryption.
	* @param m plaintext as a BigInteger
	* @param r random plaintext to help with encryption
	* @return ciphertext as a BigInteger
	*/	
	public BigInteger Encryption(BigInteger m, BigInteger r) 
	{
		return g.modPow(m, nsquare).multiply(r.modPow(n, nsquare)).mod(nsquare);	
	}
	
	/**
	* Encrypts plaintext m. ciphertext c = g^m * r^n mod n^2. This function automatically generates random input r (to help with encryption).
	* @param m plaintext as a BigInteger
	* @return ciphertext as a BigInteger
	*/
	public BigInteger Encryption(BigInteger m) 
	{
		BigInteger r = new BigInteger(bitLength, new Random());
		return g.modPow(m, nsquare).multiply(r.modPow(n, nsquare)).mod(nsquare);	
	}
	
	/**
	* Decrypts ciphertext c. plaintext m = L(c^lambda mod n^2) * u mod n, where u = (L(g^lambda mod n^2))^(-1) mod n.
	* @param c ciphertext as a BigInteger
	* @return plaintext as a BigInteger
	*/
	public BigInteger Decryption(BigInteger c) 
	{
		BigInteger u = g.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).modInverse(n);
		return c.modPow(lambda, nsquare).subtract(BigInteger.ONE).divide(n).multiply(u).mod(n);
	}
	
	/**
	* main function
	* @param str intput string
	*/
	public static void main(String[] str) 
	{
		/* instantiating an object of Paillier cryptosystem*/
		Paillier paillier = new Paillier();
		/* instantiating two plaintext msgs*/
		/* Array declaration*/
		int size;
		System.out.println("Enter the vector size");
		Scanner s = new Scanner(System.in);
		size = s.nextInt();
		
		BigInteger A[]= new BigInteger [size];
		BigInteger EA[]= new BigInteger [size];
		BigInteger B[]= new BigInteger [size];
		
		
    	Scanner f22 = new Scanner(System.in);
    	
//		String textLambda = x.toString();
//		String textMu = x.toString();
//		System.out.println("Enter the filename for Vector A");
//    	String fileName22 = f22.next() + ".txt";

		
		
		System.out.println("Enter the filename for Vector A");
    	String fileName22 = f22.next() + ".txt";
		//String B[]=new String [size];
		System.out.println("Enter all the values of vector A");
		for (int i=0; i<size;i++)
		{
			A[i]=s.nextBigInteger();
		}
		
    	File fout22 = new File(fileName22);
    	FileOutputStream fos22 = null;
		try {
			fos22 = new FileOutputStream(fout22);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bw22 = new BufferedWriter(new OutputStreamWriter(fos22));
		
		try 
		{
			for (int i = 0; i < A.length; i++)
			{
				bw22.write(A[i].toString());
				bw22.newLine();
			}			
			bw22.close();


		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
    	Scanner f33 = new Scanner(System.in);
		System.out.println("Enter the filename for Vector B");
    	String fileName33 = f33.next() + ".txt";
		System.out.println("Enter all the values of vector B");
		for (int i=0; i<size;i++)
		{
			B[i]=s.nextBigInteger();
		}
		
    	File fout33 = new File(fileName33);
    	FileOutputStream fos33 = null;
		try {
			fos33 = new FileOutputStream(fout33);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bw33 = new BufferedWriter(new OutputStreamWriter(fos33));
		
		try 
		{
			for (int i = 0; i < B.length; i++)
			{
				bw33.write(A[i].toString());
				bw33.newLine();
			}			
			bw33.close();


		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
		
		//Multiplication of two vectors
		for (int i=0; i<size;i++)
		{
			//BigInteger m1 = new BigInteger(A[i]);
			EA[i] = paillier.Encryption(A[i]);
			System.out.println("EA[i]="+EA[i]);
		}
		
    	Scanner f44 = new Scanner(System.in);
		System.out.println("Enter the filename for Encrypted U");
    	String fileName44 = f44.next() + ".txt";
		
    	File fout44 = new File(fileName44);
    	FileOutputStream fos44 = null;
		try {
			fos44 = new FileOutputStream(fout44);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bw44 = new BufferedWriter(new OutputStreamWriter(fos44));
		
		try 
		{
			for (int i = 0; i < EA.length; i++)
			{
				bw44.write(EA[i].toString());
				bw44.newLine();
			}			
			bw44.close();


		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
		
		BigInteger PowEA[]= new BigInteger [size];
		
		BigInteger prod = new BigInteger("1");
		for (int i=0; i<size;i++)
		{
			//BigInteger m1 = new BigInteger(A[i]);
			BigInteger pow=EA[i].modPow(B[i], paillier.nsquare);
			PowEA[i] = pow;
			prod=prod.multiply(pow).mod(paillier.nsquare);
		
		}
		
		
		
		System.out.println("prod="+paillier.Decryption(prod).toString()); // Final Result
		
		
    	Scanner f55 = new Scanner(System.in);
		System.out.println("Enter the filename for Encrypted dotprod of U and V");
    	String fileName55 = f55.next() + ".txt";
		
    	File fout55 = new File(fileName55);
    	FileOutputStream fos55 = null;
		try {
			fos55 = new FileOutputStream(fout55);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
     
    	BufferedWriter bw55 = new BufferedWriter(new OutputStreamWriter(fos55));
		
		try 
		{
			for (int i = 0; i < PowEA.length; i++)
			{
				bw55.write(PowEA[i].toString());
				bw55.newLine();
			}
			bw55.write("Final Dot Product = " + paillier.Decryption(prod).toString());
			bw55.close();


		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
		
	}
}
