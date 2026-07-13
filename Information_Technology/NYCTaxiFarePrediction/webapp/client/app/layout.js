import { Inter } from 'next/font/google';
import './globals.css';
import Navbar from './ui/Navbar';
import { Suspense } from 'react';
import Loading from './loading';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'NYC Taxi Fare and Trip Duration Prediction',
  icons: {
    icon: ['/favicon.ico'],
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang='en'>
      <body className={inter.className}>
        <Suspense fallback={<Loading />}>
          <Navbar />
          {children}
        </Suspense>
      </body>
    </html>
  );
}
