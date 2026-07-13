'use client';
import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { FaGithub, FaLinkedin } from 'react-icons/fa';

const myLoader = ({ src, width, quality }) => {
  return `https://avatars.githubusercontent.com/u/${src}?s=${width}`;
};

const TeamMember = ({
  name,
  profilePicture,
  githubUsername,
  linkedinUsername,
}) => {
  return (
    <div className='bg-white p-4 rounded-lg shadow-md text-center'>
      <Image
        loader={myLoader}
        src={profilePicture}
        alt={name}
        width={100}
        height={100}
        className='object-cover mx-auto mb-4 rounded-full'
      />
      <h2 className='text-lg font-bold mb-2'>{name}</h2>
      <div className='flex justify-center items-center space-x-8'>
        <Link
          href={`https://github.com/${githubUsername}`}
          target='_blank'
          rel='noopener noreferrer'
          className='text-neutral-800 hover:underline'
        >
          <FaGithub size={30} />
        </Link>
        <Link
          href={`https://www.linkedin.com/in/${linkedinUsername}`}
          target='_blank'
          rel='noopener noreferrer'
          className='text-blue-700 hover:underline'
        >
          <FaLinkedin size={30} />
        </Link>
      </div>
    </div>
  );
};

export default TeamMember;
