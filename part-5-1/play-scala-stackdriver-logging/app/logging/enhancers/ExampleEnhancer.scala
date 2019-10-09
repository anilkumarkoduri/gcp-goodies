package logging.enhancers

import com.google.cloud.logging.LogEntry
import com.google.cloud.logging.LoggingEnhancer

/*
 * Copyright 2017 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


// [START logging_enhancer]


// Add / update additional fields to the log entry
class ExampleEnhancer extends LoggingEnhancer {
  def enhanceLogEntry(logEntry: LogEntry.Builder): Unit = { // add additional labels
    logEntry.addLabel("test-label-1", "test-value-1")
  }
}

// [END logging_enhancer]