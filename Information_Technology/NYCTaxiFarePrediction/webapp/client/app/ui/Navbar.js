import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className='bg-yellow-500 p-4'>
      <div className='container mx-auto flex items-center justify-between'>
        {/* Left side - Logo/Icon */}
        <Link href={'/'} className='flex items-center'>
          <Image src='/icon.png' width={45} height={45} alt='Logo' />
        </Link>

        {/* Right side - Menu options */}
        <ul className='flex space-x-6'>
          <li className='nav-item'>
            <Link className='nav-link' href='/'>
              Home
            </Link>
          </li>
          <li className='nav-item'>
            <Link className='nav-link' href='/docs'>
              Docs
            </Link>
          </li>
          <li className='nav-item'>
            <Link className='nav-link' href='/team'>
              Team
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
