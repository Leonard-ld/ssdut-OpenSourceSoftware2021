import com.mongodb.spark.MongoSpark;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class MongoDBSparkConn {
    SparkSession spark = null;
    JavaSparkContext jsc = null;
    Dataset<Row> dataSet = null;
    MongoDBSparkConn(String database, String collection){
        spark = SparkSession.builder()
                .master("local")
                .appName("MongoSparkConnectorIntro")
                .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/"+database+"."+collection)
                .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/"+database+".test")
                .getOrCreate();
        jsc = new JavaSparkContext(spark.sparkContext());
        dataSet = MongoSpark.load(jsc).toDF();
    }

    /**
     * 执行query语句并将结果保存到dataSet中返回
     * @param statement
     * @return query语句结果
     */
    public Dataset<Row> query(String statement) {
        dataSet.createOrReplaceTempView("table");
        Dataset<Row> result = spark.sql(statement);
        return result;
    }

    /**
     * 将dataSet中的数据保存到数据库的collection表中
     * @param dataSet
     * @param collection
     */
    public void save(Dataset<Row> dataSet, String collection){
        MongoSpark.write(dataSet).option("collection", collection).mode("overwrite").save();
    }

}

