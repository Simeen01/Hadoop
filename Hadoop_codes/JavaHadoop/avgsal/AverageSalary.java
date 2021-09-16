import java.io.IOException;
import java.util.Iterable;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreducer.Job;
import org.apache.hadoop.mapreducer.Mapper;
import org.apache.hadoop.mapreducer.Reducer;
import org.apache.hadoop.mapreducer.lib.input.FileInputFormat;
import org.apache.hadoop.mapreducer.lib.output.FileOutputFormat;
import org.apache.hadoop.util.tool;
import org.apache.hadoop.util.ToolRunner;

public class AverageSalary
{
    public static class MapClass extends Mapper<LongWritable, Text, Text, IntWritable>
    {
        Text outKey = new Text();
        IntWritable outValue = new IntWritable();

        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException
        {
            String[] colmn = value.toString().split(",");
            outKey.set(colmn[2]);
            outValue.set(Integer.parseInt(colmn[3]));
            context.write(outkey, outValue);
        }
    }

    //permanent [100,300,200,400]
    public static class ReduceClass extends Reducer<Text, IntWritable, Text, IntWritable>
    {
        IntWritable outValue = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> value, Context context) throws IOException, InterruptedException
        {
            int sum = 0, count=0, avg;
            for(IntWritable sal:value)
            {
                sum = sum + sal.get();
                count++;
            }
            avg = sum/count;
            outValue.set(avg);
            context.write(key, outValue);
        }
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException
    {
        Configuration conf = new Configuration();
        String[] otherArgs = new GenericOptionParser(conf, args).getRemainingArgs();
        if(otherArgs.length != 2)
        {
            System.err.println("Number of argumeng passed is not 2");
            System.exit(1);
        }
            job job = Job.getInstance(conf, "average salary");
            job.setJar("avgsal.jar");
        job.setJarByClass(AverageSalary.class);
        job.setMapperClass(MapClass.class);
        job.setReducerClass(ReduceClass.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
        FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }

}