"use client";

import { StreamingText } from "@/components/ui/streaming-text";
import { useEffect, useState } from "react";
import { marked } from "marked";

const contents = [
  "Your privacy is important to us. This privacy statement explains the personal data Microsoft processes, how Microsoft processes it, and for what purposes.",
  "Microsoft offers a wide range of products, including server products used to help operate enterprises worldwide, devices you use in your home, software that students use at school, and services developers use to create and host what’s next. References to Microsoft products in this statement include Microsoft services, websites, apps, software, servers, and devices.",
  "Please read the product-specific details in this privacy statement, which provide additional relevant information. This statement applies to the interactions Microsoft has with you and the Microsoft products listed below, as well as other Microsoft products that display this statement.",
  "Young people may prefer starting with the Privacy for young people page. That page highlights information that may be helpful for young people.",
  "For individuals in the United States, please refer to our U.S. State Data Privacy Notice and the Consumer Health Data Privacy Policy for additional information about the processing of your personal data, and your rights under applicable U.S. state data privacy laws.",
];

export default function Home() {
  const [text, setText] = useState<string>("");
  useEffect(() => {
    let currentIndex = 0;
    const interval = setInterval(() => {
      if (currentIndex < contents.length) {
        setText((prev) => prev + (prev ? "\n\n" : "") + contents[currentIndex]);
        console.log("Adding text:", contents[currentIndex]);
        currentIndex++;
      } else {
        clearInterval(interval);
      }
    }, 5000);

    return () => clearInterval(interval);
  }, []);
  const renderer = (displayedText: string) => {
    return <div dangerouslySetInnerHTML={{ __html: marked(displayedText) }} />;
  };

  return (
    <div>
      {text ? (
        <StreamingText text={text} renderer={renderer} />
      ) : (
        <div className="text-gray-500">Loading...</div>
      )}
    </div>
  );
}
