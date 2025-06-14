"use client";
import { useEffect, useState } from "react";

interface StreamingTextProps {
  className?: string;
  text?: string;
  speed?: number;
  onComplete?: () => void;
  onChange?: (displayedText?: string, totalText?: string) => void;
  renderer?: (displayedText: string, className?: string) => React.ReactNode;
}

export function StreamingText({
  className,
  text: totalText,
  speed = 20,
  onComplete,
  onChange,
  renderer,
}: StreamingTextProps) {
  const [displayedTextLength, setDisplayedTextLength] = useState<number>(0);
  const [displayedText, setDisplayedText] = useState<string>("");

  useEffect(() => {
    if (!totalText) {
      setDisplayedTextLength(0);
      return;
    }

    if (!speed || speed <= 0) {
      setDisplayedTextLength(totalText.length);
    }

    const timeout = setTimeout(() => {
      if (displayedTextLength < totalText.length) {
        setDisplayedTextLength((prev) => prev + 1);
      } else {
        setDisplayedTextLength(totalText.length);
        onComplete?.();
      }
    }, speed || 20);

    return () => clearTimeout(timeout);
  }, [displayedTextLength, speed, totalText]);

  useEffect(() => {
    if (displayedTextLength > 0 && totalText) {
      setDisplayedText(
        displayedTextLength < totalText.length
          ? totalText.slice(0, displayedTextLength)
          : totalText
      );
    }
  }, [displayedTextLength, totalText]);

  useEffect(() => {
    onChange?.(displayedText, totalText);
  }, [displayedText, totalText, onChange]);

  return renderer ? (
    renderer(displayedText, className)
  ) : (
    <span className={className}>{displayedText}</span>
  );
}
