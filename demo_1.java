import java.io.File;
import java.io.IOException;


public class demo_1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		String separator = File.separator;
		String filename = "myfile.txt";
		String directory = "mydir1" + separator +"mydir2";
		
		File f = new File(directory,filename);
		if(f.exists()){
			System.out.println("文件名： "+f.getAbsolutePath());
			System.out.println("文件大小： "+f.length());
		}else{
			f.getParentFile().mkdirs();
			try {
				f.createNewFile();
			} catch (IOException e) {
				// TODO 自动生成的 catch 块
				e.printStackTrace();
			}
		}
	}

}
