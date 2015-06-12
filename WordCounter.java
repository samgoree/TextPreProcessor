/* WordCounter.java
 * Sam Goree
 * Counts the words fed into stdin and writes the frequencies to args[0]
 * args[0] is the output file, this can contain data already, in which case it will just be summed with the new data
 * 
 *
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;


public class WordCounter {

	@SuppressWarnings({ "unused", "resource" })
	public static void main(String[] args) throws FileNotFoundException {
		ArrayList<String> words = new ArrayList<String>();
		ArrayList<Integer> frequencies = new ArrayList<Integer>();
		
		//load old table into memory
		File table = new File(args[0]);
		Scanner tableScanner = new Scanner(table);
		String line;
		String[] wordAndFreq;
		while(tableScanner.hasNextLine()){
			line = tableScanner.nextLine();
			wordAndFreq = line.split(",");
			if(wordAndFreq.length == 2){
				words.add(wordAndFreq[0]);
				frequencies.add(new Integer(wordAndFreq[1]));
			}
		}
		
		
		//Scan the new file
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		String word;
		boolean inserted = false;
		
		while(sc.hasNext()){
			word = sc.next();
			for(int i = 0; i < words.size(); i++){
				if(words.get(i).equals(word)){
					frequencies.set(i, new Integer(frequencies.get(i).intValue()+1));
					inserted = true;
					break;
				}				
			}
			if(!inserted){
				words.add(word);
				frequencies.add(new Integer(1));
			}
			inserted = false;
		}
		
		FileOutputStream fos = new FileOutputStream(table);
		PrintStream ps = new PrintStream(fos);
		System.setOut(ps);
		
		//write it back to the output file
		for(int i = 0 ; i < words.size(); i++){
			System.out.println(words.get(i) + "," + frequencies.get(i));
		}
				
	}
	

}
