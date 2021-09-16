import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreducer.Job;
import org.apache.hadoop.mapreducer.Mapper;
import org.apache.hadoop.mapreducer.Reducer;
import org.apache.hadoop.mapreducer.lib.input.FileInputFormat;
import org.apache.hadoop.mapreducer.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class WordCount
{
    public static class Tokenizermapper extends Mapper<Object, Text, Text, IntWritable>
    {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException
        {
            //Split input text into individual words
            StringTokenizer itr = new StringTokenizer(value.toString);

            while(itr.hasMoreTokens())
            {
                //Convert the word into a string
                word.set(itr.nextToken());
                context.write(word, one);
            }
        }
    }
    /* 
    <p>Reduce function receives all the values that have same key as the input, and it outputs the key and the number of occurences of the key as the output.</p>
    */
    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable>
    {
        private void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException
        {
            int sum=0;
            for(IntWritable val : values)
            {
                sum+=val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws InterruptedException
    {
        Configuration conf = new Configuration();
        String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
        if(otherArgs.length != 2)
        {
            System.err.println("Usage: wordcount <in> <out>");
            System.exit(2);
        }
        Job job = Job.getInstance(conf, "word count");
        job.setJar("chapter1.jar");
        job.setJarByClass(WordCount.class);
        job.setMapperClass(Tokenizermapper.class);

        //Uncomment the following line to enable the Combiner
        //job.setCombinerClass(IntSumReducer.class);

        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
        FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}