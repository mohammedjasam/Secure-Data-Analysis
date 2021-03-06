package Proj3;
import java.math.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;

public class homework4 
{
	
/* All temp values are generated to write to file as per the instructions in the assignment */	
	
//	p and q are large primes
	private BigInteger p, q, pTemp, qTemp;	

//	Lambda and Mu are the private keys
	private BigInteger lambda, lambdaTemp, Mu, MuTemp;
	
//	n is the product of p and q also nsq = n*n and g is the generator. n and g together act as public keys
	public BigInteger n, nTemp, nsq, nsqTemp, g, gTemp;	

//	# of bits used in mod
	private int bitLength;
	
//	Global var which stores the size of contents in the file!
	public static int fileCount;

//	parameterized constructor to call the keygen function
	public homework4(int numBits, int probability) 
	{
		KeyGen(numBits, probability);
	}
	
//	This function reads data from the file
	@SuppressWarnings("null")
	public static String[] ReadFromFile(String fileName) throws IOException
	{
		File f = new File("./" + fileName);
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(f);		
		long arrCount = 0;
		arrCount = Files.lines(Paths.get(fileName)).count(); // len of the file content		
		String str[] = new String[(int) arrCount];
		fileCount = (int) arrCount;
		
		for (int i = 0; scan.hasNext(); i++)
		{
			String s = scan.nextLine();
			str[i] = s;
		}		
		
		return str;
	}	
	
//	This function writes data to the Files
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
		} 
		catch (IOException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
	}
	
//	Constructs the key using the specified key size
	public homework4() 
	{
		Scanner s1 = new Scanner(System.in);
		System.out.print("Enter key size: ");
		int keySize = s1.nextInt();
		KeyGen(keySize, 64);
	}
// 	This function reads pqg and generates the mu and lambda
	public void KeyGen(int numBits, int probability) 
	{
		bitLength = numBits;
		Scanner pqgFile = new Scanner(System.in);
		
//		The below block of code inputs the values of pqg from the user
		System.out.print("Enter the filename contains p, q and g: ");		
		String input[] = new String[fileCount];
		
		try {
			input = ReadFromFile(pqgFile.next() + ".txt");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		p = new BigInteger(input[0]);
		q = new BigInteger(input[1]);
		g = new BigInteger(input[2]);
		
//		Generates P and Q
		pTemp = new BigInteger(bitLength / 2, probability, new Random());
		qTemp = new BigInteger(bitLength / 2, probability, new Random());
		
		nTemp = pTemp.multiply(qTemp);
		nsqTemp = nTemp.multiply(nTemp);
		
		n = p.multiply(q);
		nsq = n.multiply(n);
		
//		Randomly generating G
		Random rnd = new Random(nsqTemp.intValue() - 1);
		BigInteger gTemp;
		do {
		    gTemp = new BigInteger(n.bitLength(), rnd);
		} while (gTemp.compareTo(n) >= 0);
		
		
		lambdaTemp = pTemp.subtract(BigInteger.ONE).multiply(qTemp.subtract(BigInteger.ONE)).divide(
		pTemp.subtract(BigInteger.ONE).gcd(qTemp.subtract(BigInteger.ONE)));
		
		lambda = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE)).divide(
		p.subtract(BigInteger.ONE).gcd(q.subtract(BigInteger.ONE)));
		
//		Verification of G.
		if (gTemp.modPow(lambdaTemp, nsqTemp).subtract(BigInteger.ONE).divide(nTemp).gcd(nTemp).intValue() != 1) 
		{
			System.out.println("Wrong G, choose a new randome value!");
			System.exit(1);
		}
		
		MuTemp = gTemp.modPow(lambdaTemp, nsqTemp).subtract(BigInteger.ONE).divide(nTemp).modInverse(nTemp);	
		
//		Created here as per the instructions!
		Mu = g.modPow(lambda, nsq).subtract(BigInteger.ONE).divide(n).modInverse(n);
		
//		Creating data to write to file
		String textP = "P = "+ pTemp + " ";
		String textQ = "\nQ = "+ qTemp + " ";
		String textG = "\nG = "+ gTemp + " ";
		
//		Scanner object to read data from console
    	Scanner f1 = new Scanner(System.in);
    	String fileName = "GeneratedPQG.txt";    	
    	
    	String[] pqg = new String[3];
    	pqg[0] = textP;
    	pqg[1] = textQ;
    	pqg[2] = textG;
    	
    	WriteToFile(fileName, pqg); // Writing P, Q, G to the file!

		String textLambda = "Lambda = " + lambda.toString();
		String textMu = "Mu = " + Mu.toString();
		System.out.print("Enter the filename to store Lamda and Mu: ");
    	String fileName2 = f1.next() + ".txt";
    	
    	String[] lambda_mu = new String[2];
    	lambda_mu[0] = textLambda;
    	lambda_mu[1] = textMu;
    	
    	WriteToFile(fileName2, lambda_mu); // Writing Lambda and Mu to the file!		
	}
	
//	Encrypts the plaintext using the public keys g and n then returns the Ciphertext
	public BigInteger Encryption(BigInteger m) 
	{
		BigInteger r = new BigInteger(bitLength, new Random());
		return g.modPow(m, nsq).multiply(r.modPow(n, nsq)).mod(nsq);	
	}
	
//	Creates the Decryption key lambda and Mu, then decrypts the Cipher text and returns the Plaintext
	public BigInteger Decryption(BigInteger c) 
	{
		lambda = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE)).divide(
		p.subtract(BigInteger.ONE).gcd(q.subtract(BigInteger.ONE)));
		Mu = g.modPow(lambda, nsq).subtract(BigInteger.ONE).divide(n).modInverse(n);
		return c.modPow(lambda, nsq).subtract(BigInteger.ONE).divide(n).multiply(Mu).mod(n);
	}	
	
	public static void main(String[] args) throws IOException 
	{		
		homework4 obj = new homework4();		
		
		int size; // Gets the size of the vectors from the console
		Scanner f1 = new Scanner(System.in);
		System.out.print("Enter the filename that contains Vector U: ");
		
		@SuppressWarnings("resource")
		Scanner VecUFile = new Scanner(System.in);
		String inputU[] = new String[fileCount];
		try 
		{

			inputU = ReadFromFile(VecUFile.next() + ".txt");


		} 
		catch (IOException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		size = fileCount;
		
//		Creating different BigInteger arrays to store the values and encrypted values of U and V respectively
		BigInteger A[]= new BigInteger [size];
		BigInteger EA[]= new BigInteger [size];
		BigInteger EB[]= new BigInteger [size];
		BigInteger B[]= new BigInteger [size];
		String VecA[] = new String[size];
		String VecB[] = new String[size];
		BigInteger PowEA[]= new BigInteger [size];		
		BigInteger prod = new BigInteger("1");
		
		for (int i=0; i<size;i++)
		{
			BigInteger x = new BigInteger(inputU[i]);
			A[i] = x;
		}

		System.out.print("Enter the filename that contains Vector V: ");
		@SuppressWarnings("resource")
		Scanner VecVFile = new Scanner(System.in);
		String inputV[] = new String[fileCount];
		try 
		{
			inputV = ReadFromFile(VecVFile.next() + ".txt");
		}
		catch (IOException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		size = fileCount;
		
//		Loop that reads the bigInteger and creates a string copy of that bigInteger!
		for (int i=0; i<size;i++)
		{
			BigInteger x = new BigInteger(inputV[i]);
			B[i]=x;
		}
		
		System.out.print("Enter the filename to store Encrypted U: ");
    	String EA_File = f1.next() + ".txt";
		String EA_Array[] = new String[size];
		
		//Multiplication of two vectors
		for (int i=0; i<size;i++)
		{
			EA[i] = obj.Encryption(A[i]);
			EA_Array[i] = "EU[" + Integer.toString(i) + "] = " + EA[i].toString();
		}
		
		WriteToFile(EA_File, EA_Array); // Writing Vector EA to the file!		
		
		System.out.print("Enter the filename for Encrypted V: ");
    	String EB_File = f1.next() + ".txt";
		String EB_Array[] = new String[size];

		for (int i=0; i<size;i++)
		{
			EB[i] = obj.Encryption(B[i]);
			EB_Array[i] = "EV[" + Integer.toString(i) + "] = " + EB[i].toString();
		}
		
		WriteToFile(EB_File, EB_Array); // Writing Vector EB to the file!				

		for (int i=0; i<size;i++)
		{
			BigInteger pow=EA[i].modPow(B[i], obj.nsq);
			PowEA[i] = pow;
			prod=prod.multiply(pow).mod(obj.nsq);		
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
			bwEAB.write("Final Dot Product = " + obj.Decryption(prod).toString());
			bwEAB.close();


		} 
		catch (IOException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
		
		System.out.println("Product = " + obj.Decryption(prod).toString()); // Final Result		
		System.out.println("All Files are now ready in the Project Folder!");
	}
}
