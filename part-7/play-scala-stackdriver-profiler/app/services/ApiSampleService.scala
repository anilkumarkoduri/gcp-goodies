package services

import javax.inject.Inject

import jp.co.bizreach.trace.{TraceData, ZipkinTraceServiceLike}

import scala.concurrent.Future

class ApiSampleService @Inject()(tracer: ZipkinTraceServiceLike) {

  def sample(url: String)(implicit traceData: TraceData): Future[String] = {
    tracer.trace("local-wait") { implicit traceData =>
      //Thread.sleep(300 + Random.nextInt(700))
      Thread.sleep(500)
      println("** end **")
    }
    println("** send **")
    Future.successful("sample called")
  }
}
